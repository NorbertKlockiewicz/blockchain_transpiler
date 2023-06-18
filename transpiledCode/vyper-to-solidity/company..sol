pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Financial events the contract logs
    event Transfer(address indexed sender, address indexed receiver, uint256 value);

    event Buy(address indexed buyer, uint256 buy_order);

    event Sell(address indexed seller, uint256 sell_order);

    event Pay(address indexed vendor, uint256 amount);

    // Initiate the variables for the company and it's own shares.
    address public company;
    uint256 public totalShares;
    uint256 public price;
    // Store a ledger of stockholder holdings.
    mapping (address => uint256) holdings;
    // Set up the company.
    // ##### VYPER DECORATORS #####
    // @external
    constructor (address _company, uint256 _total_shares, uint256 initial_price) private external
    {
        require(_total_shares > 0);
        require(initial_price > 0);
        company = _company;
        totalShares = _total_shares;
        price = initial_price;
        // The company holds all the shares at first, but can sell them all.
        holdings[company] = _total_shares;
    }


    // Public function to allow external access to _stockAvailable
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function stockAvailable() public external view returns (uint256)
    {
        return _stockAvailable();
    }


    // Give some value to the company and get stock in return.
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function buyStock() public external payable
    {
        // Note: full amount is given to company (no fractional shares),
        //       so be sure to send exact amount to buy shares
        uint256 buy_order = msg.value / price; //# rounds down
        // Check that there are enough shares to buy.
        require(_stockAvailable() >= buy_order);
        // Take the shares off the market and give them to the stockholder.
        holdings[company] -= buy_order;
        holdings[msg.sender] += buy_order;
        // Log the buy event.
        emit Buy(msg.sender, buy_order);
    }


    // Public function to allow external access to _getHolding
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function getHolding(address _stockholder) public external view returns (uint256)
    {
        return _getHolding(_stockholder);
    }


    // Return the amount the company has on hand in cash.
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function cash() public external view returns (uint256)
    {
        return balance;
    }


    // Give stock back to the company and get money back as ETH.
    // ##### VYPER DECORATORS #####
    // @external
    function sellStock(uint256 sell_order) public external
    {
        require(sell_order > 0); //# Otherwise, this would fail at send() below,
        // due to an OOG error (there would be zero value available for gas).
        // You can only sell as much stock as you own.
        require(_getHolding(msg.sender) >= sell_order);
        // Check that the company can pay you.
        require(balance >= (sell_order * price));
        // Sell the stock, send the proceeds to the user
        // and put the stock back on the market.
        holdings[msg.sender] -= sell_order;
        holdings[company] += sell_order;
        msg.sender.transfer(sell_order * price);
        // Log the sell event.
        emit Sell(msg.sender, sell_order);
    }


    // Transfer stock from one stockholder to another. (Assume that the
    // receiver is given some compensation, but this is not enforced.)
    // ##### VYPER DECORATORS #####
    // @external
    function transferStock(address receiver, uint256 transfer_order) public external
    {
        require(transfer_order > 0); //# This is similar to sellStock above.
        // Similarly, you can only trade as much stock as you own.
        require(_getHolding(msg.sender) >= transfer_order);
        // Debit the sender's stock and add to the receiver's address.
        holdings[msg.sender] -= transfer_order;
        holdings[receiver] += transfer_order;
        // Log the transfer event.
        emit Transfer(msg.sender, receiver, transfer_order);
    }


    // Allow the company to pay someone for services rendered.
    // ##### VYPER DECORATORS #####
    // @external
    function payBill(address vendor, uint256 amount) public external
    {
        // Only the company can pay people.
        require(msg.sender == company);
        // Also, it can pay only if there's enough to pay them with.
        require(balance >= amount);
        // Pay the bill!
        vendor.transfer(amount);
        // Log the payment event.
        emit Pay(vendor, amount);
    }


    // Public function to allow external access to _debt
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function debt() public external view returns (uint256)
    {
        return _debt();
    }


    // Return the cash holdings minus the debt of the company.
    // The share debt or liability only is included here,
    // but of course all other liabilities can be included.
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function worth() public external view returns (uint256)
    {
        return balance - _debt();
    }


    // Return the amount in wei that a company has raised in stock offerings.
    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _debt() private internal view returns (uint256)
    {
        return (totalShares - _stockAvailable()) * price;
    }


    // Find out how much stock the company holds
    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _stockAvailable() private internal view returns (uint256)
    {
        return holdings[company];
    }


    // Find out how much stock any address (that's owned by someone) has.
    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _getHolding(address _stockholder) private internal view returns (uint256)
    {
        return holdings[_stockholder];
    }



}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
