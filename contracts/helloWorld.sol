pragma solidity ^0.5.0;


/* define contract */

contract helloWorld {

    /* define variables, all variables are stored on the blockchain */
    string public greeting;

    function getGreeting () public returns(string memory) {
        greeting = 'Hello World';
        return greeting;
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function Greet() view public returns (string memory) {
        return greeting;
    }

}
