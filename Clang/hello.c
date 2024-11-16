// 1. Intro: Hello World program in C

// #include <stdio.h>
// int main(void)
// {
//  puts("Hello, World");
//  return 0;
// }

// Version = K&R
// #include <stdio.h>
// main()
// {
//  printf("hello, world\n");
// }

//  2. comments
#if 0 /* Starts the "comment", anything from here on is removed by preprocessor */
/* A large amount of code with multi-line comments */ 
int foo()
{
 /* lots of code */
 ...
 /* ... some comment describing the if statement ... */
 if (someTest) {
 /* some more comments */
 return 1;
 }
 return 0;
}
#endif /* 0 */
/* code from here on is "uncommented" (included in compiled executable) */

// 