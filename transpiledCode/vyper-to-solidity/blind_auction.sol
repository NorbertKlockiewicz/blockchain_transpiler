pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Blind Auction. Adapted to Vyper from [Solidity by Example](https://github.com/ethereum/solidity/blob/develop/docs/solidity-by-example.rst#blind-auction-1)
    struct Bid {
        bytes32 blindedBid;
        uint256 deposit;
    }


    // Note: because Vyper does not allow for dynamic arrays, we have limited the
    // number of bids that can be placed by one address to 128 in this example
    int128 constant MAX_BIDS = 128;
    // Event for logging that auction has ended
    event AuctionEnded(address highestBidder, uint256 highestBid);

    // Auction parameters
    address public beneficiary;
    uint256 public biddingEnd;
    uint256 public revealEnd;
    // Set to true at the end of auction, disallowing any new bids
    bool public ended;
    // Final auction state
    uint256 public highestBid;
    address public highestBidder;
    // State of the bids
    mapping (address => Bid[128]) bids;
    mapping (address => int128) bidCounts;
    // Allowed withdrawals of previous bids
    mapping (address => uint256) pendingReturns;
    // Create a blinded auction with `_biddingTime` seconds bidding time and
    // `_revealTime` seconds reveal time on behalf of the beneficiary address
    // `_beneficiary`.
    // ##### VYPER DECORATORS #####
    // @external
    constructor (address _beneficiary, uint256 _biddingTime, uint256 _revealTime) external
    {
        beneficiary = _beneficiary;
        biddingEnd = block.timestamp + _biddingTime;
        revealEnd = biddingEnd + _revealTime;
    }


    // Place a blinded bid with:
    //
    // _blindedBid = keccak256(concat(
    //       convert(value, bytes32),
    //       convert(fake, bytes32),
    //       secret)
    // )
    //
    // The sent ether is only refunded if the bid is correctly revealed in the
    // revealing phase. The bid is valid if the ether sent together with the bid is
    // at least "value" and "fake" is not true. Setting "fake" to true and sending
    // not the exact amount are ways to hide the real bid but still make the
    // required deposit. The same address can place multiple bids.
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function bid(bytes32 _blindedBid) external payable
    {
        // Check if bidding period is still open
        require(block.timestamp < biddingEnd);
        // Check that payer hasn't already placed maximum number of bids
        int128 numBids = bidCounts[msg.sender];
        require(numBids < MAX_BIDS);
        // Add bid to mapping of all bids
        bids[msg.sender][numBids] = Bid({
            blindedBid: _blindedBid,
            deposit: msg.value
        });
        bidCounts[msg.sender] += 1;
    }


    // Returns a boolean value, `True` if bid placed successfully, `False` otherwise.
    // ##### VYPER DECORATORS #####
    // @internal
    function placeBid(address bidder, uint256 _value) internal returns (bool)
    {
        // If bid is less than highest bid, bid fails
        if ((_value <= highestBid)) {
            return false;
        }
        // Refund the previously highest bidder
        if ((highestBidder != address(0))) {
            pendingReturns[highestBidder] += highestBid;
        }
        // Place bid successfully and update auction state
        highestBid = _value;
        highestBidder = bidder;
        return true;
    }


    // Reveal your blinded bids. You will get a refund for all correctly blinded
    // invalid bids and for all bids except for the totally highest.
    // ##### VYPER DECORATORS #####
    // @external
    function reveal(int128 _numBids, uint256[128] _values, bool[128] _fakes, bytes32[128] _secrets) external
    {
        // Check that bidding period is over
        require(block.timestamp > biddingEnd);
        // Check that reveal end has not passed
        require(block.timestamp < revealEnd);
        // Check that number of bids being revealed matches log for sender
        require(_numBids == bidCounts[msg.sender]);
        // Calculate refund for sender
        uint256 refund = 0;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < MAX_BIDS; i++) {
            // Note that loop may break sooner than 128 iterations if i >= _numBids
            if ((i >= _numBids)) {
                break;
            }
            // Get bid to check
            Bid bidToCheck = (bids[msg.sender])[i];
            // Check against encoded packet
            uint256 value = _values[i];
            bool fake = _fakes[i];
            bytes32 secret = _secrets[i];
            bytes32 blindedBid = keccak256(concat(convert(value, bytes32), convert(fake, bytes32), secret));
            // Bid was not actually revealed
            // Do not refund deposit
            require(blindedBid == bidToCheck.blindedBid);
            // Add deposit to refund if bid was indeed revealed
            refund += bidToCheck.deposit;
            if ((!fake && bidToCheck.deposit >= value)) {
                if ((placeBid(msg.sender, value))) {
                    refund -= value;
                }
            }
            // Make it impossible for the sender to re-claim the same deposit
            bytes32 zeroBytes32 = bytes32(0);
            bidToCheck.blindedBid = zeroBytes32;
        }


        // Send refund if non-zero
        if ((refund != 0)) {
            msg.sender.transfer(refund);
        }
    }


    // Withdraw a bid that was overbid.
    // ##### VYPER DECORATORS #####
    // @external
    function withdraw() external
    {
        // Check that there is an allowed pending return.
        uint256 pendingAmount = pendingReturns[msg.sender];
        if ((pendingAmount > 0)) {
            // If so, set pending returns to zero to prevent recipient from calling
            // this function again as part of the receiving call before `transfer`
            // returns (see the remark above about conditions -> effects ->
            // interaction).
            pendingReturns[msg.sender] = 0;
            // Then send return
            msg.sender.transfer(pendingAmount);
        }
    }


    // End the auction and send the highest bid to the beneficiary.
    // ##### VYPER DECORATORS #####
    // @external
    function auctionEnd() external
    {
        // Check that reveal end has passed
        require(block.timestamp > revealEnd);
        // Check that auction has not already been marked as ended
        require(!ended);
        // Log auction ending and set flag
        emit AuctionEnded(highestBidder, highestBid);
        ended = true;
        // Transfer funds to beneficiary
        beneficiary.transfer(highestBid);
    }



}

