pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    interface Exchange {
        function token() external view returns (ERC20);
        function receive(address _from, uint256 _amt) external nonpayable;
        function transfer(address _to, uint256 _amt) external nonpayable;
    }
    bytes32 public exchange_codehash;

    mapping (ERC20 => Exchange) public exchanges;

    // ##### VYPER DECORATORS #####
    // @external
    constructor (bytes32 _exchange_codehash) external 
    {
        exchange_codehash = _exchange_codehash;
    }

    // ##### VYPER DECORATORS #####
    // @external
    function register() external 
    {
        require(msg.sender.codehash == exchange_codehash);
        Exchange exchange = Exchange(msg.sender);
        exchanges[exchange.token()] = exchange;
    }

    // ##### VYPER DECORATORS #####
    // @external
    function trade(ERC20 _token1, ERC20 _token2, uint256 _amt) external 
    {
        exchanges[_token1].receive(msg.sender, _amt);
        exchanges[_token2].transfer(msg.sender, _amt);
    }


}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
// fromvyper.interfacesimportERC20
