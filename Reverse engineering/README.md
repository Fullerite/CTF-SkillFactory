
# Reverse engineering

### 1st step
Firstly, I converted the unknown extension `main` to `main.elf` and found out that there is function `main` by using `strings main.elf`

![Function main](https://im.wampi.ru/2023/02/18/func_main.png)

### 2nd step
Then I decompiled `main` using **IDA** (free version)

I noticed that user input is compared with the `result` variable using the `strncmp` function when verifying access, and also that the `result` variable is first encrypted by XORing its data with hexadecimal 0x63 (decimal 99)

![Function main decompiled](https://ic.wampi.ru/2023/02/18/func_main_decompiled.png)

### 3rd step
Finally, I went to IDA View and found data written in the `result` variable (lines 4060-4088) and decrypted it by reverse XORing

![Result variable](https://ie.wampi.ru/2023/02/18/result_var.png)