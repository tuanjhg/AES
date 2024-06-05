from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from Crypto.Cipher import AES
from django.conf import settings
import os

def home:
    return render('home.html')

def get_key(request):
    if request.method == "POST":
        key = request.POST.get('key')
        if len(key) != 16:
            return HttpResponseBadRequest("The key must be exactly 16 characters long.")
        return key.encode()  # Return the key as bytes
    return render(request, 'upload.html')

def handle_uploaded_file(uploaded_file):
    file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    return file_path

def encrypt(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(nonce)
        file.write(tag)
        file.write(ciphertext)
    return encrypted_file_path

def decrypt(file_path, key, new_filename):
    with open(file_path, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    # Ensure the new filename is secure
    new_filename = os.path.basename(new_filename)  # Sanitize the input to prevent directory traversal
    new_file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
    
    with open(new_file_path, 'wb') as file:
        file.write(plaintext)
    return new_file_path

def encrypt_file(request):
    if request.method == 'POST' and 'encrypt' in request.POST:
        uploaded_file = request.FILES['file']
        file_path = handle_uploaded_file(uploaded_file)
        key = get_key(request)
        if isinstance(key, HttpResponseBadRequest):
            return key
        encrypted_file_path = encrypt(file_path, key)
        context = {'file_path': encrypted_file_path}
        return render(request, 'down.html', context)
    return render(request, 'encrypt.html')

def decrypt_file(request):
    if request.method == 'POST' and 'decrypt' in request.POST:
        uploaded_file = request.FILES['file']
        file_path = handle_uploaded_file(uploaded_file)
        key = get_key(request)
        if isinstance(key, HttpResponseBadRequest):
            return key
        new_filename = request.POST.get('new_filename')
        decrypted_file_path = decrypt(file_path, key, new_filename)
        context = {'file_path': decrypted_file_path}
        return render(request, 'down1.html', context)
    return render(request, 'decrypt.html')
