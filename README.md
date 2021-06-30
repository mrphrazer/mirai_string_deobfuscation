# Mirai String Decryption
Author: **Tim Blazytko**

_Demonstrates how to decrypt strings in Mirai samples_

## Description:

Script and malware sample to decrypt strings in a Mirai malware sample.

Implementation is based on Binary Ninja. Check out the following blog post for more information:

[Automation in Reverse Engineering: String Decryption](https://synthesis.to/2021/06/30/automating_string_decryption.html)

## Usage

* Open `sample/mirai_arm` in Binary Ninja
* Load and execute the script

To test the script with other Mirai samples, replace the function address in the following line:

```
target_function = bv.get_function_at(0x10778)
```

## Contact

For more information, contact [@mr_phrazer](https://twitter.com/mr_phrazer).

