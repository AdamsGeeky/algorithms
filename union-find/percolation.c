#include "percolation_header.h"


void _init_p(pc *p)
{
	int i, j;

	init_uf(pc->uf);

	for (i = 0; i < p->size; ++i)
	{
		for (j = 0; j < p->size; ++j)
			p->grid[i][j] = 0;
		union(0, i, pc->uf);
		union(pc->uf->size - 1, p->size - 1 + i);
	}
}


void open(int i, int j, pc *p)
{
	int a, b;

	if (pc->grid[i][j] == 1)
		return;

	a = ;
	b = ;
	grid[i][j] = 1;
	if (i > 0)
		_union(a, b, p->uf);
