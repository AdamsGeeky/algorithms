#include "ufheader.h"
#include <stdio.h>


/**
 * init_uf - initialize all values
 * @qu: pointer to ufw struct
 *
 */
void init_uf(ufw *qu)
{
	int i;

	for (i = 0; i < qu->size; ++i)
	{
		qu->parent[i] = i;
		qu->weight[i] = 0;
	}
}



/**
 * connected - check if 2 sites are connected
 * @p: a site
 * @q: another site
 * @qu: pointer to struct
 * Return: 1 if true, 0 otherwise
 */
int connected(int p, int q, ufw *qu)
{
	return(find(p, qu) == find(q, qu));
}


/**
 * find - find the root of a site
 * @p: a site
 * @qu: a pointer to the struct
 * Return: the root
 */
int find(int p, ufw *qu)
{
	if (p < 0 || p > qu->size - 1)
	{
		puts("error p value");
		return (-1);
	}

	while (p != qu->parent[p])
		p = qu->parent[p];

	return (p);
}

/**
 * _union - connect 2 sites
 * @p: a site
 * @q: another site
 * @qu: a pointer to the struct
 */
void _union(int p, int q, ufw *qu)
{
	int root_p, root_q;

	if (p < 0 || p > qu->size - 1)
	{
		puts("error p value");
		return;
	}
	if (q < 0 || q > qu->size - 1)
	{
		puts("error q value");
		return;
	}

	root_p = find(p, qu);
	root_q = find(q, qu);
	if(root_p == root_q)
		return;

	qu->parent[root_p] = root_q;
}
