pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Safe Remote Purchase
    // Originally from
    // https://github.com/ethereum/solidity/blob/develop/docs/solidity-by-example.rst
    // Ported to vyper and optimized.
    // Rundown of the transaction:
    // 1. Seller posts item for sale and posts safety deposit of double the item value.
    //    Balance is 2*value.
    //    (1.1. Seller can reclaim deposit and close the sale as long as nothing was purchased.)
    // 2. Buyer purchases item (value) plus posts an additional safety deposit (Item value).
    //    Balance is 4*value.
    // 3. Seller ships item.
    // 4. Buyer confirms receiving the item. Buyer's deposit (value) is returned.
    //    Seller's deposit (2*value) + items value is returned. Balance is 0.
    uint256 public value;
    //#Value of the item
    address public seller;
    address public buyer;
    bool public unlocked;
    bool public ended;
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    constructor () private external payable
    {
        require((msg.value % 2) == 0);
        value = msg.value / 2; // # The seller initializes the contract by
        // posting a safety deposit of 2*value of the item up for sale.
        seller = msg.sender;
        unlocked = true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function abort() public external
    {
        require(unlocked); //#Is the contract still refundable?
        require(msg.sender == seller); //# Only the seller can refund
        // his deposit before any buyer purchases the item.
        selfdestruct(seller); //# Refunds the seller and deletes the contract.
    }


    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function purchase() public external payable
    {
        require(unlocked); //# Is the contract still open (is the item still up for sale)?
        require(msg.value == (2 * value)); //# Is the deposit the correct value?
        buyer = msg.sender;
        unlocked = false;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function received() public external
    {
        // 1. Conditions
        require(!unlocked); //# Is the item already purchased and pending confirmation from the buyer?
        require(msg.sender == buyer);
        require(!ended);
        // 2. Effects
        ended = true;
        // 3. Interaction
        buyer.transfer(value); //# Return the buyer's deposit (=value) to the buyer.
        selfdestruct(seller); //# Return the seller's deposit (=2*value) and the purchase price (=value) to the seller.
    }



}

