#include <stdio.h>
#include "ufheader.h"

/**
 * _init - initialize all values
 * @qu: pointer to uf struct
 *
 */
void init_uf(uf *qu)
{
	for (int i = 0; i < qu->size; ++i)
	{
		qu->array[i] = i;
	}
}


/**
 * find - find the root of a site
 * @p: a site
 * Return: the root
 * In quick union the root is just the value at index
 */
int find(int p, uf *qu)
{
	if (p < 0 || p > qu->size - 1)
	{
		puts("error p value");
		return (-1);
	}
	return (qu->array[p]);
}


/**
 * _union - connect 2 sites
 * @p: first site
 * @q: second site
 * @uf: pointer to uf struct
 * in quick union, if the values are different I have to
 * loop through the array to change all roots
 */
void _union(int p, int q, uf *qu)
{
	int tmp, i;

	if (p < 0 || p > qu->size - 1)
	{
		puts("error p value");
		return;
	}
	if (p < 0 || p > qu->size - 1)
	{
		puts("error q value");
		return;
	}
	if (find(p, qu) == find(q, qu))
		return;

	tmp = qu->array[p];
	for (i = 0; i < qu->size; ++i)
	{
		if (find(i, qu) == tmp)
			qu->array[i] = qu->array[q];
	}
}

/**
 * connected - check if 2 sites are connected
 * @p: a site
 * @q: another site
 * @qu: pointer to struct
 * Return: 1 if true, 0 otherwise
 */
int connected(int p, int q, uf *qu)
{
	return(find(p, qu) == find(q, qu));
}
