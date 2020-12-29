const HelloWorld = artifacts.require('helloWorld');

contract('HelloWorldContract', () => {
  it('Should deploy smart contract properly', async () => {
    //Checking if deployed
    const helloWorld = await HelloWorld.deployed();
    console.log('Succesfully Deployed at Address: ', helloWorld.address);
    assert(helloWorld.address!=='');
  });
  it("Deploy 'Hello World' properly", async () => {
    //Checking if deployed
    const helloWorld = await HelloWorld.deployed();
    const result = await helloWorld.getGreeting();
    assert(result === 'Hello World');
  });



});
