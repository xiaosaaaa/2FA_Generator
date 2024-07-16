# 2FA_Generator
The project is used to generate 2FA code
![image](https://github.com/user-attachments/assets/95121328-fc89-4ba3-bde7-ae94b6840200)

## 1. Introdcue
1. This project only supports TOTP(Time-based One-time Password)
2. If you enter the seed in the .env file, it will show the verification codes on the web and refresh them automatically, and the project currently supports a maximum of four seeds simultaneously.
3. If you do not enter a seed, or if you do not enter at least one valid seed, this section will be automatically hidden, Only the 2FA generation function can be used. 
## 2. How to use it
if you can connect to dockerhub, just`docker-compose up -d`      
if you can't, you should follow these steps.
1. `wget https://github.com/xiaosaaaa/2FA_Generator/releases/download/0.0.1/2FA_Generator.tar`
2. `docker load -i 2FA_Generator.tar`
3. `docker-compose up -d`
## 3. support amd64/armv8
amd64:  
2FA_Generator.tar  
image: xiaosaaaa/2fa_generator:latest

armv8:  
2FA_Generator_arm.tar  
image: xiaosaaaa/2fa_generator_arm:latest
## 4. support QR code


