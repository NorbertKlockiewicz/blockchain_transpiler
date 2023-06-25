pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // Voting with delegation.
    // Information about voters
    struct Voter {
        // weight is accumulated by delegation
        int128 weight;
        // if true, that person already voted (which includes voting by delegating)
        bool voted;
        // person delegated to
        address delegate;
        // index of the voted proposal, which is not meaningful unless `voted` is True.
        int128 vote;
    }


    // Users can create proposals
    struct Proposal {
        // short name (up to 32 bytes)
        bytes32 name;
        // number of accumulated votes
        int128 voteCount;
    }


    mapping (address => Voter) public voters;
    mapping (int128 => Proposal) public proposals;
    int128 public voterCount;
    address public chairperson;
    int128 public int128Proposals;
    enum E { A, B, C }

    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _delegated(address addr) internal view returns (bool)
    {
        return voters[addr].delegate != address(0);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function delegated(address addr) external view returns (bool)
    {
        return _delegated(addr);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _directlyVoted(address addr) internal view returns (bool)
    {
        return voters[addr].voted && (voters[addr].delegate == address(0));
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function directlyVoted(address addr) external view returns (bool)
    {
        return _directlyVoted(addr);
    }


    // Setup global variables
    // ##### VYPER DECORATORS #####
    // @external
    constructor (bytes32[2] _proposalNames) external
    {
        chairperson = msg.sender;
        voterCount = 0;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < 2; i++) {
            proposals[i] = Proposal({
                name: _proposalNames[i],
                voteCount: 0
            });
            int128Proposals += 1;
        }


    }


    // Give a `voter` the right to vote on this ballot.
    // This may only be called by the `chairperson`.
    // ##### VYPER DECORATORS #####
    // @external
    function giveRightToVote(address voter) external
    {
        // Throws if the sender is not the chairperson.
        require(msg.sender == chairperson);
        // Throws if the voter has already voted.
        require(!voters[voter].voted);
        // Throws if the voter's voting weight isn't 0.
        require(voters[voter].weight == 0);
        voters[voter].weight = 1;
        voterCount += 1;
    }


    // Used by `delegate` below, callable externally via `forwardWeight`
    // ##### VYPER DECORATORS #####
    // @internal
    function _forwardWeight(address delegate_with_weight_to_forward) internal
    {
        require(_delegated(delegate_with_weight_to_forward));
        // Throw if there is nothing to do:
        require(voters[delegate_with_weight_to_forward].weight > 0);
        address target = voters[delegate_with_weight_to_forward].delegate;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < 4; i++) {
            if (_delegated(target)) {
                target = voters[target].delegate;
                // The following effectively detects cycles of length <= 5,
                // in which the delegation is given back to the delegator.
                // This could be done for any int128ber of loops,
                // or even infinitely with a while loop.
                // However, cycles aren't actually problematic for correctness;
                // they just result in spoiled votes.
                // So, in the production version, this should instead be
                // the responsibility of the contract's client, and this
                // check should be removed.
                require(target != delegate_with_weight_to_forward);
            }            else
            // Weight will be moved to someone who directly voted or
            // hasn't voted.
            break;

        }


        int128 weight_to_forward = voters[delegate_with_weight_to_forward].weight;
        voters[delegate_with_weight_to_forward].weight = 0;
        voters[target].weight += weight_to_forward;
        if (_directlyVoted(target)) {
            proposals[voters[target].vote].voteCount += weight_to_forward;
            voters[target].weight = 0;
        }
        // To reiterate: if target is also a delegate, this function will need
        // to be called again, similarly to as above.
    }


    // Public function to call _forwardWeight
    // ##### VYPER DECORATORS #####
    // @external
    function forwardWeight(address delegate_with_weight_to_forward) external
    {
        _forwardWeight(delegate_with_weight_to_forward);
    }


    // Delegate your vote to the voter `to`.
    // ##### VYPER DECORATORS #####
    // @external
    function delegate(address to) external
    {
        // Throws if the sender has already voted
        require(!voters[msg.sender].voted);
        // Throws if the sender tries to delegate their vote to themselves or to
        // the default address value of 0x0000000000000000000000000000000000000000
        // (the latter might not be problematic, but I don't want to think about it).
        require(to != msg.sender);
        require(to != address(0));
        voters[msg.sender].voted = true;
        voters[msg.sender].delegate = to;
        // This call will throw if and only if this delegation would cause a loop
        // of length <= 5 that ends up delegating back to the delegator.
        _forwardWeight(msg.sender);
    }


    // Give your vote (including votes delegated to you)
    // to proposal `proposals[proposal].name`.
    // ##### VYPER DECORATORS #####
    // @external
    function vote(int128 proposal) external
    {
        // can't vote twice
        require(!voters[msg.sender].voted);
        // can only vote on legitimate proposals
        require(proposal < int128Proposals);
        voters[msg.sender].vote = proposal;
        voters[msg.sender].voted = true;
        // transfer msg.sender's weight to proposal
        proposals[proposal].voteCount += voters[msg.sender].weight;
        voters[msg.sender].weight = 0;
    }


    // Computes the winning proposal taking all
    // previous votes into account.
    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    function _winningProposal() internal view returns (int128)
    {
        int128 winning_vote_count = 0;
        int128 winning_proposal = 0;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < 2; i++) {
            if (proposals[i].voteCount > winning_vote_count) {
                winning_vote_count = proposals[i].voteCount;
                winning_proposal = i;
            }
        }


        return winning_proposal;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function winningProposal() external view returns (int128)
    {
        return _winningProposal();
    }


    // Calls winningProposal() function to get the index
    // of the winner contained in the proposals array and then
    // returns the name of the winner
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function winnerName() external view returns (bytes32)
    {
        return proposals[_winningProposal()].name;
    }



}

