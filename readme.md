This Program is only tested on MacOS. Other OS like Windows or Linux could have problems with the python imports.

* Create a virtual Python environment (Version <= 3.7) and activate it. Afterwards install the requirements with:

```
pip install -r requirements.txt
```

* To execute the Q# Decrypter you have to install at least .NET Core SDK 3.1 or higher. Then execute:
```
dotnet tool install -g Microsoft.Quantum.IQSharp
dotnet iqsharp install --user
```
If this fails make sure the `.dotnet/tools` folder is in your path (usually in your home folder)

* To execute the IBMDecrypterReal you have to add a `account.py` file in the parent directory with the content
```
token = '<Your IBM Token>'
```


If you execute it via the Python Notebook you can't run the QSharpDecryptor from Microsoft, due to unavailable support of the Notebooks.

To run the programm execute the `run.py` file. 
There are 3 possible arguments: 
* `-o` or `--option` (required):
    * The Decryptor you want to start. There are 4 possibilities
        * "numeric"
        * "ibmq"
        * "ibmqreal"
        * "qsharp"
* `-f` or `--factor` (optional):
    * The factor which is being used for the n of the RSA. This is implemented for all possible cases till n = 65:
        * 15
        * 21
        * 33
        * 35
        * 39
        * 51
        * 55
        * 65
* `-k` or `--keysize` (optional):
    * The keysize you want to use for the RSA (only used for the NumericDecryptor)

**IMPORTANT**: To execute the run.py file you have to `cd` into the subdirectory Quantum-RSA-Decryptor, otherwise the namespace of the Q#-File is incorrect.
```
cd Quantum-RSA-Decryptor/
python run.py -o <option> -f <factor> -k <keysize>
```