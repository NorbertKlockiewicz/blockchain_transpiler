// TODO: FIX IMPORT fromvyper.interfacesimportERC20
// TODO: FIX IMPORT fromvyper.interfacesimportERC20Detailed
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // @dev Implementation of ERC-20 token standard.
    // @author Takayuki Jimba (@yudetamago)
    // https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md
// TODO: FIX IMPORT fromvyper.interfacesimportERC20

// TODO: FIX IMPORT fromvyper.interfacesimportERC20Detailed

    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC20
    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC20Detailed
    event Transfer(address indexed sender, address indexed receiver, uint256 value);

    event Approval(address indexed owner, address indexed spender, uint256 value);

    string[32] public name;
    string[32] public symbol;
    uint8 public decimals;
    // NOTE: By declaring `balanceOf` as public, vyper automatically generates a 'balanceOf()' getter
    //       method to allow access to account balances.
    //       The _KeyType will become a required parameter for the getter and it will return _ValueType.
    //       See: https://vyper.readthedocs.io/en/v0.1.0-beta.8/types.html?highlight=getter#mappings
    mapping (address => uint256) public balanceOf;
    // By declaring `allowance` as public, vyper automatically generates the `allowance()` getter
    mapping (address => mapping (address => uint256)) public allowance;
    // By declaring `totalSupply` as public, we automatically create the `totalSupply()` getter
    uint256 public totalSupply;
    address minter;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (string[32] _name, string[32] _symbol, uint8 _decimals, uint256 _supply) private external
    {
        uint256 init_supply = _supply * 10 ** convert(_decimals, uint256);
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        balanceOf[msg.sender] = init_supply;
        totalSupply = init_supply;
        minter = msg.sender;
        emit Transfer(address(0), msg.sender, init_supply);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Transfer token for a specified address
    @param _to The address to transfer to.
    @param _value The amount to be transferred.
    */
    function transfer(address _to, uint256 _value) public external returns (bool)
    {
        // NOTE: vyper does not allow underflows
        //       so the following subtraction would revert on insufficient balance
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
     @dev Transfer tokens from one address to another.
     @param _from address The address which you want to send tokens from
     @param _to address The address which you want to transfer to
     @param _value uint256 the amount of tokens to be transferred
    */
    function transferFrom(address _from, address _to, uint256 _value) public external returns (bool)
    {
        // NOTE: vyper does not allow underflows
        //       so the following subtraction would revert on insufficient balance
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        // NOTE: vyper does not allow underflows
        //      so the following subtraction would revert on insufficient allowance
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Approve the passed address to spend the specified amount of tokens on behalf of msg.sender.
         Beware that changing an allowance with this method brings the risk that someone may use both the old
         and the new allowance by unfortunate transaction ordering. One possible solution to mitigate this
         race condition is to first reduce the spender's allowance to 0 and set the desired value afterwards:
         https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
    @param _spender The address which will spend the funds.
    @param _value The amount of tokens to be spent.
    */
    function approve(address _spender, uint256 _value) public external returns (bool)
    {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Mint an amount of the token and assigns it to an account.
         This encapsulates the modification of balances such that the
         proper events are emitted.
    @param _to The account that will receive the created tokens.
    @param _value The amount that will be created.
    */
    function mint(address _to, uint256 _value) public external
    {
        require(msg.sender == minter);
        require(_to != address(0));
        totalSupply += _value;
        balanceOf[_to] += _value;
        emit Transfer(address(0), _to, _value);
    }


    // ##### VYPER DECORATORS #####
    // @internal
    /**
    @dev Internal function that burns an amount of the token of a given
         account.
    @param _to The account whose tokens will be burned.
    @param _value The amount that will be burned.
    */
    function _burn(address _to, uint256 _value) private internal
    {
        require(_to != address(0));
        totalSupply -= _value;
        balanceOf[_to] -= _value;
        emit Transfer(_to, address(0), _value);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Burn an amount of the token of msg.sender.
    @param _value The amount that will be burned.
    */
    function burn(uint256 _value) public external
    {
        _burn(msg.sender, _value);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Burn an amount of the token from a given account.
    @param _to The account whose tokens will be burned.
    @param _value The amount that will be burned.
    */
    function burnFrom(address _to, uint256 _value) public external
    {
        allowance[_to][msg.sender] -= _value;
        _burn(_to, _value);
    }



}

