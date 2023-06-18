// TODO: FIX IMPORT fromvyper.interfacesimportERC20
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
// TODO: FIX IMPORT fromvyper.interfacesimportERC20

    uint256 public totalEthQty;
    uint256 public totalTokenQty;
    // Constant set in `initiate` that's used to calculate
    // the amount of ether/tokens that are exchanged
    uint256 public invariant;
    ERC20 token_address;
    address public owner;
    // Sets the on chain market maker with its owner, intial token quantity,
    // and initial ether quantity
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function initiate(address token_addr, uint256 token_quantity) public external payable
    {
        require(invariant == 0);
        token_address = ERC20(token_addr);
        token_address.transferFrom(msg.sender, this, token_quantity);
        owner = msg.sender;
        totalEthQty = msg.value;
        totalTokenQty = token_quantity;
        invariant = msg.value * token_quantity;
        require(invariant > 0);
    }


    // Sells ether to the contract in exchange for tokens (minus a fee)
    // ##### VYPER DECORATORS #####
    // @external
    // @payable
    function ethToTokens() public external payable
    {
        uint256 fee = msg.value / 500;
        uint256 eth_in_purchase = msg.value - fee;
        uint256 new_total_eth = totalEthQty + eth_in_purchase;
        uint256 new_total_tokens = invariant / new_total_eth;
        token_address.transfer(msg.sender, totalTokenQty - new_total_tokens);
        totalEthQty = new_total_eth;
        totalTokenQty = new_total_tokens;
    }


    // Sells tokens to the contract in exchange for ether
    // ##### VYPER DECORATORS #####
    // @external
    function tokensToEth(uint256 sell_quantity) public external
    {
        token_address.transferFrom(msg.sender, this, sell_quantity);
        uint256 new_total_tokens = totalTokenQty + sell_quantity;
        uint256 new_total_eth = invariant / new_total_tokens;
        uint256 eth_to_send = totalEthQty - new_total_eth;
        msg.sender.transfer(eth_to_send);
        totalEthQty = new_total_eth;
        totalTokenQty = new_total_tokens;
    }


    // Owner can withdraw their funds and destroy the market maker
    // ##### VYPER DECORATORS #####
    // @external
    function ownerWithdraw() public external
    {
        require(owner == msg.sender);
        token_address.transfer(owner, totalTokenQty);
        selfdestruct(owner);
    }



}

