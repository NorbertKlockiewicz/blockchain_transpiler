interface Factory {
    function register() public external nonpayable;
}
// TODO: FIX IMPORT fromvyper.interfacesimportERC20
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
// TODO: FIX IMPORT fromvyper.interfacesimportERC20

    ERC20 public token;
    Factory factory;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (ERC20 _token, Factory _factory) private external
    {
        token = _token;
        factory = _factory;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function initialize() public external
    {
        // Anyone can safely call this function because of EXTCODEHASH
        factory.register();
    }


    // NOTE: This contract restricts trading to only be done by the factory.
    //       A practical implementation would probably want counter-pairs
    //       and liquidity management features for each exchange pool.
    // ##### VYPER DECORATORS #####
    // @external
    function receive(address _from, uint256 _amt) public external
    {
        require(msg.sender == factory.address);
        bool success = token.transferFrom(_from, this, _amt);
        require(success);
    }


    // ##### VYPER DECORATORS #####
    // @external
    function transfer(address _to, uint256 _amt) public external
    {
        require(msg.sender == factory.address);
        bool success = token.transfer(_to, _amt);
        require(success);
    }



}

