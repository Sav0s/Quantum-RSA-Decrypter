* To execute the Q# Decrypter you have to install at least .NET Core SDK 3.1 or higher. Then execute

```
dotnet tool install -g Microsoft.Quantum.IQSharp
dotnet iqsharp install --user
```

* To execute the IBM Decrypter you have to add a `acount.py` file in the parent directory with the content
```
token = '<Your IBM Token>'
```