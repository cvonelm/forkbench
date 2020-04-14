Generates a chain of fork and execing applications to test the behaviour of tracing applications

First generate the chain like this, where depth is the depth of the chain:

```sh
./bench chain [depth]
```

Then compile and start it like this:
```sh
cd build
make
./test1
```
