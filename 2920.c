#pragma warning(disable 4996)
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int a[8];
	int ass = 0;
	int dss = 0;
	for (int i = 0; i < 8; i++){
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < 8; i++) {
		if (a[i] == i + 1)
		{
			ass++;
		}
		else if (a[i] == 8 - i)
		{
			dss++;
		}
		else
			break;
	}
	if (ass == 8)
		printf("ascending");
	else if (dss == 8)
		printf("descending");
	else
		printf("mixed");
}