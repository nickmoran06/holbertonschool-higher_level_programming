#include "lists.h"

/**
 * insert_node - inserts a new node at a given position.
 *
 * @head: first node od the list
 * @number: index to insert a number
 *
 * Return: the address of the new node,
 * or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *cpy = NULL;
	listint_t *ref = NULL;


	if (!head)
		return (0);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);

	new->n = number;
	if (!*head || number <= 0)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	cpy = *head;
	while (cpy)
	{
		if (cpy->n < number)
		{
			ref = cpy;
			cpy = cpy->next;
		}
		else
			break;
	}
	new->next = ref->next;
	ref->next = new;

	return (new);
}
