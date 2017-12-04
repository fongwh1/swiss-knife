CROSS_COMPILE=
CC=$(CROSS_COMPILE)gcc
LDD=ldd

LIB_INJECTION=libinjection.so
TRANS_LIB_INJECTION=libtransinjection.so
BIN=main

all: run

main: main.c
	$(CC) main.c -o $(BIN)

run: main injection.c
	$(CC) -shared -fPIC injection.c -o $(LIB_INJECTION)
	LD_PRELOAD=$(PWD)/$(LIB_INJECTION) ./$(BIN)

run_dl: main
	$(CC) -shared -fPIC transparent_injection.c -o $(TRANS_LIB_INJECTION) -ldl
	LD_PRELOAD=$(PWD)/$(TRANS_LIB_INJECTION) ./$(BIN)

clean:
	@rm $(LIB_INJECTION) $(TRANS_LIB_INJECTION) $(BIN)