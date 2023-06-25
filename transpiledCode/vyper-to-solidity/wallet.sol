pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // An example of how you can do a wallet in Vyper.
    // Warning: NOT AUDITED. Do not use to store substantial quantities of funds.
    // A list of the owners addresses (there are a maximum of 5 owners)
    address[5] public owners;
    // The number of owners required to approve a transaction
    int128 threshold;
    // The number of transactions that have been approved
    int128 public seq;
    // ##### VYPER DECORATORS #####
    // @external
    constructor (address[5] _owners, int128 _threshold) external
    {
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < 5; i++) {
            if (_owners[i] != address(0)) {
                owners[i] = _owners[i];
            }
        }


        threshold = _threshold;
    }


    // ##### VYPER DECORATORS #####
    // @external
    function testEcrecover(bytes32 h, uint256 v, uint256 r, uint256 s) external returns (address)
    {
        return ecrecover(h, v, r, s);
    }


    // `@payable` allows functions to receive ether
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function approve(int128 _seq, address to, uint256 _value, bytes[4096] data, uint256[3][5] sigdata) external payable returns (bytes[4096])
    {
        // Throws if the value sent to the contract is less than the sum of the value to be sent
        require(msg.value >= _value);
        // Every time the number of approvals starts at 0 (multiple signatures can be added through the sigdata argument)
        int128 approvals = 0;
        // Starts by combining:
        // 1) The number of transactions approved thus far.
        // 2) The address the transaction is going to be sent to (can be a contract or a user).
        // 3) The value in wei that will be sent with this transaction.
        // 4) The data to be sent with this transaction (usually data is used to deploy contracts or to call functions on contracts, but you can put whatever you want in it).
        // Takes the keccak256 hash of the combination
        bytes32 h = keccak256(concat(convert(_seq, bytes32), convert(to, bytes32), convert(_value, bytes32), data));
        // Then we combine the Ethereum Signed message with our previous hash
        // Owners will have to sign the below message
        bytes32 h2 = keccak256(concat(bytes("\x19Ethereum Signed Message:\n32"), h));
        // Verifies that the caller of approve has entered the correct transaction number
        require(seq == _seq);
        // # Iterates through all the owners and verifies that there signatures,
        // # given as the sigdata argument are correct
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < 5; i++) {
            if (sigdata[i][0] != 0) {
                // If an invalid signature is given for an owner then the contract throws
                require(ecrecover(h2, sigdata[i][0], sigdata[i][1], sigdata[i][2]) == owners[i]);
                // For every valid signature increase the number of approvals by 1
                approvals += 1;
            }
        }


        // Throw if the number of approvals is less then the number of approvals required (the threshold)
        require(approvals >= threshold);
        // The transaction has been approved
        // Increase the number of approved transactions by 1
        seq += 1;
        // Use raw_call to send the transaction
        return raw_call(to, data, max_outsize = 4096, gas = 3000000, value = _value);
    }


    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    fallback() external payable
    {
    }



}

