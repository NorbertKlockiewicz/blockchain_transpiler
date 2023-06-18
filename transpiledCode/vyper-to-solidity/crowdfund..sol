pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Setup private variables (only callable from within the contract)
    mapping (address => uint256) funders;
    address beneficiary;
    uint256 public deadline;
    uint256 public goal;
    uint256 public timelimit;
    // Setup global variables
    // ##### VYPER DECORATORS #####
    // @external
    constructor (address _beneficiary, uint256 _goal, uint256 _timelimit) private external
    {
        beneficiary = _beneficiary;
        deadline = block.timestamp + _timelimit;
        timelimit = _timelimit;
        goal = _goal;
    }


    // Participate in this crowdfunding campaign
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function participate() public external payable
    {
        require(
            block.timestamp < deadline,
            "deadline not met (yet)"
        );
        funders[msg.sender] += msg.value;
    }


    // Enough money was raised! Send funds to the beneficiary
    // ##### VYPER DECORATORS #####
    // @external
    function finalize() public external
    {
        require(
            block.timestamp >= deadline,
            "deadline has passed"
        );
        require(
            balance >= goal,
            "the goal has not been reached"
        );
        selfdestruct(beneficiary);
    }


    // Let participants withdraw their fund
    // ##### VYPER DECORATORS #####
    // @external
    function refund() public external
    {
        require(block.timestamp >= deadline && balance < goal);
        require(funders[msg.sender] > 0);
        uint256 value = funders[msg.sender];
        funders[msg.sender] = 0;
        msg.sender.transfer(value);
    }



}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
