#include "ufheader.h"

/**
 * pc - struct for percolation
 * @grid: size * size matrix
 * @uf: union-find array of size size + 2
 * @size: size of thing
 */
typedef struct pc
{
	int **grid;
	ufw *uf;
	int size;
} pc;
