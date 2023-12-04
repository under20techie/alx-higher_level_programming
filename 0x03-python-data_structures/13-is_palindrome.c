#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: ptr to the head of the list.
 *
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int n = 0, i = 0;
	listint_t *current = *head, *first_half = *head, *second_half = NULL;

	if (*head == NULL)
		return (1);
	if (!head)
		return (1);
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current = *head;
	while (current && i < ((n / 2) + 1))
	{
		current  = current->next;
		i++;
	}
	if (n % 2)
		current = current->next;
	i = 0;
	second_half = rev_list(&current);

	while (i < (n / 2) && second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;

	}
	return (1);
}

/**
 * rev_list - reverses the list
 * @head: pointerto the head of the list
 *
 * Return: pointer to the head of the list or NULL
 */
listint_t *rev_list(listint_t **head)
{
	listint_t *prev = NULL, *next;

	if (!head || !*head)
		return (NULL);
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	return (*head = prev);
}
