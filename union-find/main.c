#include <stdio.h>
#include "ufheader.h"


/**
 * helper - helper for demo
 * @p: an int
 * @q: another int
 * @ufs: pointer to struc
 */
void helper(int p, int q, ufw *ufs)
{
	if(!connected(p, q, ufs))
	{
		_union(p, q, ufs);
/*		printf("new pair %i - %i\n", p, q);*/
	}
}


/**
 * main - test the code for union find
 *
 * Return: always 0
 */
int main(void)
{
	ufw ufs;
	int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int b[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

	ufs.size = 10;
	ufs.parent = a;
	ufs.weight = b;
	print_line(&ufs);
	helper(4, 3, &ufs);
	print_line(&ufs);
	helper(3, 8, &ufs);
	print_line(&ufs);
	helper(6, 5, &ufs);
	print_line(&ufs);
	helper(9, 4, &ufs);
	print_line(&ufs);
	helper(2, 1, &ufs);
	print_line(&ufs);
	helper(8, 9, &ufs);
	print_line(&ufs);
	helper(5, 0, &ufs);
	print_line(&ufs);
	helper(7, 2, &ufs);
	print_line(&ufs);
	helper(6, 1, &ufs);
	print_line(&ufs);
	helper(1, 0, &ufs);
	print_line(&ufs);
	helper(6, 7, &ufs);
	print_line(&ufs);

	return (0);
}

/**
 * print_array - print the array
 * @ufs: pointer to struct
 *
 */
void print_array(ufw *ufs)
{
	int i;

	for (i = 0; i < ufs->size; ++i)
		printf("array[%i] = %i\n", i, ufs->parent[i]);
}

/**
 * print_line - print the array
 * @ufs: pointer to struct
 *
 */
void print_line(ufw *ufs)
{
	int i;

	for (i = 0; i < ufs->size; ++i)
		printf("%i  ", ufs->parent[i]);
	puts("");
}
