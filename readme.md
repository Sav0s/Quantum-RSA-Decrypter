* Create a virtual Python environment (Version >= 3.7) and activate it. Afterwards install the requirements with:

```
pip install -r requirements.txt
```

* To execute the Q# Decrypter you have to install at least .NET Core SDK 3.1 or higher. Then execute:
```
dotnet tool install -g Microsoft.Quantum.IQSharp
dotnet iqsharp install --user
```
If this fails make sure the `.dotnet/tools` folder is in your path (usually in your home folder)

* To execute the IBM Decrypter you have to add a `acount.py` file in the parent directory with the content
```
token = '<Your IBM Token>'
```
