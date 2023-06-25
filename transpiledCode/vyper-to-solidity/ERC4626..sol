// TODO: FIX IMPORT fromvyper.interfacesimportERC20
// TODO: FIX IMPORT fromvyper.interfacesimportERC4626
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // NOTE: Copied from https://github.com/fubuloubu/ERC4626/blob/1a10b051928b11eeaad15d80397ed36603c2a49b/contracts/VyperVault.vy
    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC20
    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC4626
    //#### ERC20 #####
    uint256 public totalSupply;
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    string[10] constant NAME = "Test Vault";
    string[5] constant SYMBOL = "vTEST";
    uint8 constant DECIMALS = 18;
    event Transfer(address indexed sender, address indexed receiver, uint256 amount);

    event Approval(address indexed owner, address indexed spender, uint256 allowance);

    //#### ERC4626 #####
    ERC20 public asset;
    event Deposit(address indexed depositor, address indexed receiver, uint256 assets, uint256 shares);

    event Withdraw(address indexed withdrawer, address indexed receiver, address indexed owner, uint256 assets, uint256 shares);

    // ##### VYPER DECORATORS #####
    // @external
    constructor (ERC20 asset) private external
    {
        asset = asset;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function name() public external view returns (string[10])
    {
        return NAME;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function symbol() public external view returns (string[5])
    {
        return SYMBOL;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function decimals() public external view returns (uint8)
    {
        return DECIMALS;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function transfer(address receiver, uint256 amount) public external returns (bool)
    {
        balanceOf[msg.sender] -= amount;
        balanceOf[receiver] += amount;
        emit Transfer(msg.sender, receiver, amount);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function approve(address spender, uint256 amount) public external returns (bool)
    {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function transferFrom(address sender, address receiver, uint256 amount) public external returns (bool)
    {
        allowance[sender][msg.sender] -= amount;
        balanceOf[sender] -= amount;
        balanceOf[receiver] += amount;
        emit Transfer(sender, receiver, amount);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function totalAssets() public external view returns (uint256)
    {
        return asset.balanceOf(this);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _convertToAssets(uint256 shareAmount) private internal view returns (uint256)
    {
        uint256 totalSupply = totalSupply;
        if (totalSupply == 0) {
            return 0;
        }
        // NOTE: `shareAmount = 0` is extremely rare case, not optimizing for it
        // NOTE: `totalAssets = 0` is extremely rare case, not optimizing for it
        return shareAmount * asset.balanceOf(this) / totalSupply;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function convertToAssets(uint256 shareAmount) public external view returns (uint256)
    {
        return _convertToAssets(shareAmount);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _convertToShares(uint256 assetAmount) private internal view returns (uint256)
    {
        uint256 totalSupply = totalSupply;
        uint256 totalAssets = asset.balanceOf(this);
        if (totalAssets == 0 || totalSupply == 0) {
            return assetAmount; // # 1:1 price
        }
        // NOTE: `assetAmount = 0` is extremely rare case, not optimizing for it
        return assetAmount * totalSupply / totalAssets;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function convertToShares(uint256 assetAmount) public external view returns (uint256)
    {
        return _convertToShares(assetAmount);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function maxDeposit(address owner) public external view returns (uint256)
    {
        return max_value(uint256);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function previewDeposit(uint256 assets) public external view returns (uint256)
    {
        return _convertToShares(assets);
    }


    // ##### VYPER DECORATORS #####
    // @external
    function deposit(uint256 assets, address receiver = msg.sender) public external returns (uint256)
    {
        uint256 shares = _convertToShares(assets);
        asset.transferFrom(msg.sender, this, assets);
        totalSupply += shares;
        balanceOf[receiver] += shares;
        emit Deposit(msg.sender, receiver, assets, shares);
        return shares;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function maxMint(address owner) public external view returns (uint256)
    {
        return max_value(uint256);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function previewMint(uint256 shares) public external view returns (uint256)
    {
        uint256 assets = _convertToAssets(shares);
        // NOTE: Vyper does lazy eval on `and`, so this avoids SLOADs most of the time
        if (assets == 0 && asset.balanceOf(this) == 0) {
            return shares; // # NOTE: Assume 1:1 price if nothing deposited yet
        }
        return assets;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function mint(uint256 shares, address receiver = msg.sender) public external returns (uint256)
    {
        uint256 assets = _convertToAssets(shares);
        if (assets == 0 && asset.balanceOf(this) == 0) {
            assets = shares; // # NOTE: Assume 1:1 price if nothing deposited yet
        }
        asset.transferFrom(msg.sender, this, assets);
        totalSupply += shares;
        balanceOf[receiver] += shares;
        emit Deposit(msg.sender, receiver, assets, shares);
        return assets;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function maxWithdraw(address owner) public external view returns (uint256)
    {
        return max_value(uint256); // # real max is `self.asset.balanceOf(self)`
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function previewWithdraw(uint256 assets) public external view returns (uint256)
    {
        uint256 shares = _convertToShares(assets);
        // NOTE: Vyper does lazy eval on and, so this avoids SLOADs most of the time
        if (shares == assets && totalSupply == 0) {
            return 0; // # NOTE: Nothing to redeem
        }
        return shares;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function withdraw(uint256 assets, address receiver = msg.sender, address owner = msg.sender) public external returns (uint256)
    {
        uint256 shares = _convertToShares(assets);
        // NOTE: Vyper does lazy eval on `and`, so this avoids SLOADs most of the time
        if (shares == assets && totalSupply == 0) {
            revert ""; // # Nothing to redeem
        }
        if (owner != msg.sender) {
            allowance[owner][msg.sender] -= shares;
        }
        totalSupply -= shares;
        balanceOf[owner] -= shares;
        asset.transfer(receiver, assets);
        emit Withdraw(msg.sender, receiver, owner, assets, shares);
        return shares;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function maxRedeem(address owner) public external view returns (uint256)
    {
        return max_value(uint256); // # real max is `self.totalSupply`
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function previewRedeem(uint256 shares) public external view returns (uint256)
    {
        return _convertToAssets(shares);
    }


    // ##### VYPER DECORATORS #####
    // @external
    function redeem(uint256 shares, address receiver = msg.sender, address owner = msg.sender) public external returns (uint256)
    {
        if (owner != msg.sender) {
            allowance[owner][msg.sender] -= shares;
        }
        uint256 assets = _convertToAssets(shares);
        totalSupply -= shares;
        balanceOf[owner] -= shares;
        asset.transfer(receiver, assets);
        emit Withdraw(msg.sender, receiver, owner, assets, shares);
        return assets;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function DEBUG_steal_tokens(uint256 amount) public external
    {
        // NOTE: This is the primary method of mocking share price changes
        // do not put in production code!!!
        asset.transfer(msg.sender, amount);
    }



}

