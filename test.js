var test = [1, 2, 3];
test[100] = 8;
console.log(test);

test = ["test", "oki", "doki"];
console.log("non revers", test);
var rev_test = test.reverse();
console.log(rev_test, test);
