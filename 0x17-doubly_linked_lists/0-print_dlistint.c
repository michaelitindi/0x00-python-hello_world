#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_dlistint - print elements of a list
 * @h: pointer to head node
 * return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *current = h;
size_t i = 0;
while (current != NULL)
{
printf("%d\n", current->n);
current = current->next;
i++;
}
return (i);
}
