pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    mapping (bytes[100] => address) registry;
    // ##### VYPER DECORATORS #####
    // @external
    function register(bytes[100] name, address owner) public external
    {
        require(registry[name] == address(0)); // # check name has not been set yet.
        registry[name] = owner;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function lookup(bytes[100] name) public external view returns (address)
    {
        return registry[name];
    }




}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
