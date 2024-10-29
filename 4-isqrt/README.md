### Integer square root

Considere o algorítimo a seguir que calcula raiz quadrada de um número inteiro, 
e implemente a função em VM que faca o mesmo.

``` python
unsigned int isqrt(unsigned int y)
{
	// initial underestimate, L <= isqrt(y)
	unsigned int L = 0;
    
	while ((L + 1) * (L + 1) <= y) 
		L = L + 1;

	return L;
}
```

