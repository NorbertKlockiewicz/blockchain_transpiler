pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    event DataChange(address indexed setter, int128 value);

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
        require(
            _x >= 0,
            "No negative values"
        );
        require(
            storedData < 100,
            "Storage is locked when 100 or more is stored"
        );
        storedData = _x;
        emit DataChange(msg.sender, _x);
    }


    // ##### VYPER DECORATORS #####
    // @external
    function reset() external
    {
        storedData = 0;
    }




}

