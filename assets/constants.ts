// We are using eslint disable here for multilines because we have used quotes
// around properties at a lot of places so it is not possible to use
// "eslint disable next line" for each of them.
/* eslint-disable oppia/no-multiline-disable */
/* eslint-disable quote-props */
/* eslint-disable quotes */
/* Don't modify anything outside the {} brackets.
 * Insides of the {} brackets should be formatted as a JSON object.
 * JSON rules:
 * 1. All keys and string values must be enclosed in double quotes.
 * 2. Each key/value pair should be on a new line.
 * 3. All values and keys must be constant, you can't use any Javascript
 *    functions.
 */

/**
 * @fileoverview Initializes constants for the Oppia codebase.
 */

import {constants} from '../extensions/classifiers/proto/constants';
var fs = require('fs');
var data = fs.readFileSync('assets/constants.json', 'utf8');

data = JSON.parse(data);
console.log(data);

const constants_list = new constants();

function deepCopy(obj) {

 if(typeof obj === 'object') {
  return Object.keys(obj)
   .map(k => ({ [k]: deepCopy(obj[k]) }))
   .reduce((a, c) => Object.assign(a, c), {});
 }

 else if(Array.isArray(obj)) {
  return obj.map(deepCopy)
 }
 return obj;
}



constants_list.CAN_SEND_ANALYTICS_EVENTS = true;

console.log(constants_list['CAN_SEND_ANALYTICS_EVENTS'])

// const constants_list = constants.fromJSON(data);
// console.log(constants_list)

export default constants_list;
