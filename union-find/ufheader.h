#ifndef _UFHEADER_H_
#define _UFHEADER_H_

#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define UNIONSIZE 2000000

/**
 * struct uf - structure for union find
 * @array: a pointer to an array
 * @size: size of array
 *
 */
typedef struct uf
{
	int *array;
	int size;
} uf;

/**
 * struct uf - structure for union find
 * @parent: the array containing the parents
 * @weight: pointer to array containing weight of tree
 * with root at index
 * @size: size of array
 *
 */
typedef struct ufw
{
	int *parent;
	int *weight;
	int size;
} ufw;


/*intialize values in array*/
void init_uf(ufw *);

/*are indexes connected*/
int connected(int, int, ufw *);

/*add a connection between 2 sites*/
void _union(int, int, ufw *);

/*find the identifier (root) of site*/
int find(int, ufw *);

/*print the struct*/
void print_array(ufw *ufs);
void print_line(ufw *ufs);







#endif
