pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    int128 public storedData;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (int128 _x) private external
    {
        storedData = _x;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function set(int128 _x) public external
    {
        storedData = _x;
    }




}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
