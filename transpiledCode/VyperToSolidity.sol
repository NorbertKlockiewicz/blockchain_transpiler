pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    enum Roles { ADMIN, USER }
    struct Bid {
        bytes32 blindedBid;
        uint256 deposit;
    }

    int128 constant MAX_BIDS = 128;
    event AuctionEnded(address highestBidder, uint256 highestBid);
    event Test();
    address public beneficiary;

    uint256 public biddingEnd;

    uint256 public revealEnd;

    bool public ended;

    uint256 public highestBid;

    address public highestBidder;

    mapping (address => Bid) bids;

    mapping (address => int128) bidCounts;

    mapping (address => uint256) pendingReturns;

    // ##### VYPER DECORATORS #####
    // @external
    constructor (address _beneficiary, uint256 _biddingTime, uint256 _revealTime) external 
    {
        beneficiary = _beneficiary;
        biddingEnd = block.timestamp + _biddingTime;
        revealEnd = biddingEnd + _revealTime;
    }

    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    // @noreentrant('key')
    bool internal bidReentrancyLock = False;
    function bid(bytes32 _blindedBid) external payable
    {
        // Reentrancy lock
        require(!bidReentrancyLock, "No re-entrancy");
        bidReentrancyLock = true;

        require(block.timestamp < biddingEnd);
        int128 numBids = bidCounts[msg.sender];
        require(numBids < MAX_BIDS);
        bids[msg.sender][numBids] = Bid({
            blindedBid: _blindedBid,
            deposit: msg.value
        });
        bidCounts[msg.sender] += 1;

        // Reentrancy unlock
        bidReentrancyLock = false;
    }

    // ##### VYPER DECORATORS #####
    // @internal
    function placeBid(address bidder, uint256 _value) internal  returns (bool)
    {
        
        if (_value <= highestBid) {
            return false;
        }

        
        if (highestBidder != address(0)) {
            pendingReturns[highestBidder] += highestBid;
        }

        highestBid = _value;
        highestBidder = bidder;
        return true;
    }

    // ##### VYPER DECORATORS #####
    // @external
    function reveal(int128 _numBids, uint256 _values, bool _fakes, bytes32 _secrets) external 
    {
        require(block.timestamp > biddingEnd);
        require(block.timestamp < revealEnd);
        require(_numBids == bidCounts[msg.sender]);
        uint256 refund = 0;
        
        for (uint i = 0; i < MAX_BIDS; i++) {
            
            if (i >= _numBids) {
                break;
            }

            Bid bidToCheck = (bids[msg.sender])[i];
            uint256 value = _values[i];
            bool fake = _fakes[i];
            bytes32 secret = _secrets[i];
            bytes32 blindedBid = keccak256(concat(convert(value, bytes32), convert(fake, bytes32), secret));
            require(blindedBid == bidToCheck.blindedBid);
            refund += bidToCheck.deposit;
            
            if (!fake && bidToCheck.deposit >= value) {
                
                if (placeBid(msg.sender, value)) {
                    refund -= value;
                }

            }

            bytes32 zeroBytes32 = bytes32(0);
            bidToCheck.blindedBid = zeroBytes32;
        }

        
        if (refund != 0) {
            msg.sender.transfer(refund);
        }

    }

    // ##### VYPER DECORATORS #####
    // @external
    function withdraw() external 
    {
        uint256 pendingAmount = pendingReturns[msg.sender];
        
        if (pendingAmount > 0) {
            pendingReturns[msg.sender] = 0;
            msg.sender.transfer(pendingAmount);
        }

    }

    // ##### VYPER DECORATORS #####
    // @external
    function auctionEnd() external 
    {
        require(block.timestamp > revealEnd);
        require(!ended);
        ended = true;
        beneficiary.transfer(highestBid);
    }


}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
