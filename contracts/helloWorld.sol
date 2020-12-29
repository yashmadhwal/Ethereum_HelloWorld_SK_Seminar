pragma solidity ^0.5.0;


/* define contract */

contract helloWorld {

    /* define variables, all variables are stored on the blockchain */
    string greeting;

    function getGreeting() pure public returns(string memory) {
        return 'Hello World';
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function Greet() view public returns (string memory) {
        return greeting;
    }

}
