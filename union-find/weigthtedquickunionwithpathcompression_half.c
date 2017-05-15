#include "ufheader.h"
#include <stdio.h>
/*uses tree size to measure weight*/

/**
 * init_uf - initialize all values
 * @quw: pointer to uf struct
 *
 */
void init_uf(ufw *qu)
{
	int i;

	for (i = 0; i < qu->size; ++i)
	{
		qu->parent[i] = i;
		qu->weight[i] = 1;
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

	/*this is where we can have path compression*/

	/*path halving*/
	while (p != qu->parent[p])
	{
		/* I shorten the path in half by going
		 * directly to the parent of the parent
		 */
		qu->parent[p] = qu->parent[qu->parent[p]];
		p = qu->parent[p];
	}

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

	/*this is where the weight makes the difference*/
	if (qu->weight[root_q] >= qu->weight[root_p])
	{
		qu->parent[root_p] = root_q;
		qu->weight[root_q] += qu->weight[root_p];
	}
	else
	{
		qu->parent[root_q] = root_p;
		qu->weight[root_p] += qu->weight[root_q];
	}
}
