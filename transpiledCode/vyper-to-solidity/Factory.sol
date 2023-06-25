interface Exchange {
    function token() external view returns (ERC20);
    function receive(address _from, uint256 _amt) external nonpayable;
    function transfer(address _to, uint256 _amt) external nonpayable;
}
// TODO: FIX IMPORT fromvyper.interfacesimportERC20
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    bytes32 public exchange_codehash;
    // Maps token addresses to exchange addresses
    mapping (ERC20 => Exchange) public exchanges;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (bytes32 _exchange_codehash) external
    {
        // Register the exchange code hash during deployment of the factory
        exchange_codehash = _exchange_codehash;
    }


    // NOTE: Could implement fancier upgrade logic around self.exchange_codehash
    //       For example, allowing the deployer of this contract to change this
    //       value allows them to use a new contract if the old one has an issue.
    //       This would trigger a cascade effect across all exchanges that would
    //       need to be handled appropiately.
    // ##### VYPER DECORATORS #####
    // @external
    function register() external
    {
        // Verify code hash is the exchange's code hash
        require(msg.sender.codehash == exchange_codehash);
        // Save a lookup for the exchange
        // NOTE: Use exchange's token address because it should be globally unique
        // NOTE: Should do checks that it hasn't already been set,
        //       which has to be rectified with any upgrade strategy.
        Exchange exchange = Exchange(msg.sender);
        exchanges[exchange.token()] = exchange;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function trade(ERC20 _token1, ERC20 _token2, uint256 _amt) external
    {
        // Perform a straight exchange of token1 to token 2 (1:1 price)
        // NOTE: Any practical implementation would need to solve the price oracle problem
        exchanges[_token1].receive(msg.sender, _amt);
        exchanges[_token2].transfer(msg.sender, _amt);
    }



}

