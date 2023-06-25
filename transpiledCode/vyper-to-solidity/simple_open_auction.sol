pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Open Auction
    // Auction params
    // Beneficiary receives money from the highest bidder
    address public beneficiary;
    uint256 public auctionStart;
    uint256 public auctionEnd;
    // Current state of auction
    address public highestBidder;
    uint256 public highestBid;
    // Set to true at the end, disallows any change
    bool public ended;
    // Keep track of refunded bids so we can follow the withdraw pattern
    mapping (address => uint256) public pendingReturns;
    // Create a simple auction with `_auction_start` and
    // `_bidding_time` seconds bidding time on behalf of the
    // beneficiary address `_beneficiary`.
    // ##### VYPER DECORATORS #####
    // @external
    constructor (address _beneficiary, uint256 _auction_start, uint256 _bidding_time) external
    {
        beneficiary = _beneficiary;
        auctionStart = _auction_start; // # auction start time can be in the past, present or future
        auctionEnd = auctionStart + _bidding_time;
        require(block.timestamp < auctionEnd); //# auction end time should be in the future
    }


    // Bid on the auction with the value sent
    // together with this transaction.
    // The value will only be refunded if the
    // auction is not won.
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function bid() external payable
    {
        // Check if bidding period has started.
        require(block.timestamp >= auctionStart);
        // Check if bidding period is over.
        require(block.timestamp < auctionEnd);
        // Check if bid is high enough
        require(msg.value > highestBid);
        // Track the refund for the previous high bidder
        pendingReturns[highestBidder] += highestBid;
        // Track new high bid
        highestBidder = msg.sender;
        highestBid = msg.value;
    }


    // Withdraw a previously refunded bid. The withdraw pattern is
    // used here to avoid a security issue. If refunds were directly
    // sent as part of bid(), a malicious bidding contract could block
    // those refunds and thus block new higher bids from coming in.
    // ##### VYPER DECORATORS #####
    // @external
    function withdraw() external
    {
        uint256 pending_amount = pendingReturns[msg.sender];
        pendingReturns[msg.sender] = 0;
        msg.sender.transfer(pending_amount);
    }


    // End the auction and send the highest bid
    // to the beneficiary.
    // ##### VYPER DECORATORS #####
    // @external
    function endAuction() external
    {
        // It is a good guideline to structure functions that interact
        // with other contracts (i.e. they call functions or send Ether)
        // into three phases:
        // 1. checking conditions
        // 2. performing actions (potentially changing conditions)
        // 3. interacting with other contracts
        // If these phases are mixed up, the other contract could call
        // back into the current contract and modify the state or cause
        // effects (Ether payout) to be performed multiple times.
        // If functions called internally include interaction with external
        // contracts, they also have to be considered interaction with
        // external contracts.
        // 1. Conditions
        // Check if auction endtime has been reached
        require(block.timestamp >= auctionEnd);
        // Check if this function has already been called
        require(!ended);
        // 2. Effects
        ended = true;
        // 3. Interaction
        beneficiary.transfer(highestBid);
    }



}

