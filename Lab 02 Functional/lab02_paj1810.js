// Name : Prem Atul Jethwa
// Id: 1001861810
// Due Date: 03/07/2023
// Netid: paj1810

//Creating an array named inputtable having values from 1 to 10 as it's element
const inputtable = new Array(10)
console.log("")

console.log("********** Question 1:-  Print the inputtable array **********")
//function used to print inputtable elements
const i_array = inputtable.fill(null).map((_, i) => ++i);
console.log(i_array)
console.log("")

console.log("********** Question 2a:- Set of multiples of 5 between 1 and 51: fiveTable **********")
//function takes element's from inputtable array and multiplies each element with 5 and then prints the elements
const fiveTable = inputtable.fill(null).map((_, i) => ++i * 5);
console.log(fiveTable)
console.log("")

console.log("********** Question 2b:- Set of multiples of 13 between 1 and 131: thirteenTable **********")
//function takes elements from inputtable array and multiplies each element with 13 and then prints the elements
const thirteenTable = inputtable.fill(null).map((_, i) => ++i * 13);
console.log(thirteenTable)
console.log("")

console.log("********** Question 2c:- Set of squares of the numbers in inputtable array: squaresTable **********")
//function takes elements from inputtable array and multiplies each element with itself to get the square of the elements
const squaresTable = inputtable.fill(null).map((_, i) => ++i * i);
console.log(squaresTable)
console.log("")

console.log("********** Question 3:- Odd multiples of 5 between 1 and 100 **********")
const input = new Array(100)
const odd_multiple = input.fill(null).map((_, i) => ++i);           // function takes 100 elements in the array 
const num_5 = odd_multiple.filter(x => x % 5 === 0)                   // function filters all the multiples of 5 from the array
const result = num_5.filter(item => item % 2 == 1);                 // function that filters only the odd multiples of 5 present in array num_5
console.log(result);                                                // printing the result
console.log("")

console.log("********** Question 4:- Sum of even multiples of 7 between 1 and 100 **********")
const input_100 = new Array(100)
const n = input_100.fill(null).map((_, i) => ++i);                   // function takes 100 elements in the array 
const num_7 = n.filter(x => x % 7 === 0)                               // function filters all the multiples of 7 from the array
const num_even = num_7.filter(item => item % 2 == 0);                // function that filters only the even multiples of 7 present in array num_7
const sum = num_even.reduce((total, item) => total + item);          // function performs addition of elements present in array num_even
console.log(num_even);
console.log("")
console.log(sum);                                                    // printing the result
console.log("")

console.log("********** Question 5:- Currying Function **********")
const currying = r => h => 3.14 * r * r * h;                        // function preforming the calculation 
const intance = currying(5);                                        // assigning the value of 'r'
console.log("5a:- r=5 and h=10")
console.log(intance(10));                                           // 5-a: assigning the value of 'h'
console.log("5b:- r=5 and h=17")
console.log(intance(17));                                           // 5-b: assigning the value of 'h'
console.log("5c:- r=5 and h=11")
console.log(intance(11));                                           // 5-c: assigning the value of 'h'
console.log("")

console.log("********** Question 6:- Closures to wrap content with HTML tags **********")
// defining the mag tag funtion
makeTag = function (beginTag, endTag) {
    return function (textcontent) {
        return beginTag + textcontent + endTag;
    }
}
const tableTag = makeTag('<table>' + '\n', '</table>');            // creating the table tag
const tableData = makeTag('<td>', '</td>');                      // creating the data tag
const tableRow = makeTag('<tr>' + '\n', '</tr>' + '\n');             // creating the row tag
const tableHeader = makeTag('<th>', '</th>');                    // creating the header tag

const header1 = tableHeader('Name');                             // assigning value to header tag
const header2 = tableHeader('Major');                            // assigning value to header tag
const header3 = tableHeader('Year');                             // assigning value to header tag
const headFinal = header1 + '\n' + header2 + '\n' + header3 + '\n';    // getting all the tag together into one const variable

const name_1 = tableData('Prem Jethwa');                         // assigning value to header tag
const major_1 = tableData('Computer Science');                   // assigning value to header tag
const year_1 = tableData(2021);                                  // assigning value to header tag
const S1 = name_1 + '\n' + major_1 + '\n' + year_1 + '\n';

const name_2 = tableData('Albert Einstein');                     // assigning value to header tag
const major_2 = tableData('Physics');                            // assigning value to header tag
const year_2 = tableData(1879);                                  // assigning value to header tag
const S2 = name_2 + '\n' + major_2 + '\n' + year_2 + '\n';

const r1 = tableRow(headFinal);
const r2 = tableRow(S1);
const r3 = tableRow(S2);
const rD = r1 + '\n' + r2 + '\n' + r3;

const t = tableTag(rD);
console.log(t);
console.log("")

console.log("********** Question 7:- Generic version of questions 3 and 4 **********")
const genericfuntion = m => {
    const g_input = new Array(100)                                      // creating an array having values from 1 to 100 as it's element
    const g_array = g_input.fill(null).map((_, i) => ++i);
    const g_multiple = g_array.filter(z => z % m === 0)                   // function to the multiples of value assigned to z by user

    return (comp) => {
        if (comp === 'even') {
            return g_multiple.filter(x => x % 2 === 0)                    // Getting the even multiples of value z   

        }

        else if (comp === 'odd') {
            return g_multiple.filter(x => x % 2 === 1)                    // Getting the odd multiples of value z 
        }
        else {
            console.log("Error in Input")                               // If input other then even or odd is provided the display error
        }
    }
}
// Passing the value to main generic function
console.log("Generic version of question 3")
const for5 = genericfuntion(5)
const resultofinput = for5('odd')
console.log(resultofinput)

// Passing other option as value to main generic function
console.log("Generic version of question 4")
const for7 = genericfuntion(7)
const resultofinput2 = for7('even')
const sum_1 = num_even.reduce((total, item) => total + item);          // function performs addition of elements present in array num_even
console.log(sum_1);
console.log(resultofinput2)





