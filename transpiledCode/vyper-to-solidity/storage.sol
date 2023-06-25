pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    int128 public storedData;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (int128 _x) external
    {
        storedData = _x;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function set(int128 _x) external
    {
        storedData = _x;
    }




}

