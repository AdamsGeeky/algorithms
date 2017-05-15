#include "ufheader.h"

int main(void)
{
	int i;
	ufw *uf;

	int *rng1, *rng2, *rng3, *rng4;

	uf = malloc(sizeof(ufw));
	uf->size = UNIONSIZE;
	if (!uf)
		return (-1);
	uf->parent = malloc(sizeof(int) * UNIONSIZE);
	if (!uf->parent)
		return (-1);
	uf->weight = malloc(sizeof(int) * UNIONSIZE);
	if (!uf->weight)
		return (-1);

	rng1 = malloc(sizeof(int) * UNIONSIZE);
	rng2 = malloc(sizeof(int) * UNIONSIZE);
	rng3 = malloc(sizeof(int) * UNIONSIZE);
	rng4 = malloc(sizeof(int) * UNIONSIZE);
/* buid arrays of UNIONSIZE random numbers */
	srand(time(NULL));
	for (i = 0; i < UNIONSIZE; ++i)
	{
		rng1[i] = rand() % UNIONSIZE;
		rng2[i] = rand() % UNIONSIZE;
		rng3[i] = rand() % UNIONSIZE;
		rng4[i] = rand() % UNIONSIZE;
	}

	/*begin clockkeeping*/
	clock_t tic = clock();

	init_uf(uf);
	/* run unions from array rng1 and rng2*/
	for (i =0; i < UNIONSIZE; ++i)
	{
		_union(rng1[i], rng2[i], uf);
	}
/* run connection test from rng3 and rng4*/
	for (i =0; i < UNIONSIZE; ++i)
	{
		connected(rng3[i], rng4[i], uf);
	}


/*end clockkeeping*/
	clock_t toc = clock();
	printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);

	return (0);
}
