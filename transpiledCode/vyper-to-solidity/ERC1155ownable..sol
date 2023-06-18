interface IERC1155Receiver {
    function onERC1155Received(address operator, address sender, uint256 id, uint256 amount, bytes[CALLBACK_NUMBYTES] data) public external payable returns (bytes32);
    function onERC1155BatchReceived(address operator, address sender, uint256[] ids, uint256[] amounts, bytes[CALLBACK_NUMBYTES] data) public external payable returns (bytes4);
}
interface IERC1155MetadataURI {
    function uri(uint256 id) public external view returns (string[MAX_URI_LENGTH]);
}
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // @version >=0.3.4
    /**
    @dev Implementation of ERC-1155 non-fungible token standard ownable, with approval, OPENSEA compatible (name, symbol)
    @author Dr. Pixel (github: @Doc-Pixel)
    */

    //############## imports ###############

    //############## variables ###############
    // maximum items in a batch call. Set to 128, to be determined what the practical limits are.
    uint256 constant BATCH_SIZE = 128;
    // callback number of bytes
    uint256 constant CALLBACK_NUMBYTES = 4096;
    // URI length set to 300. 
    uint256 constant MAX_URI_LENGTH = 300;
    // for uint2str / dynamic URI
    uint256 constant MAX_DYNURI_LENGTH = 78;
    // for the .json extension on the URL
    uint256 constant MAX_EXTENSION_LENGTH = 5;
    uint256 constant MAX_URL_LENGTH = MAX_URI_LENGTH + MAX_DYNURI_LENGTH + MAX_EXTENSION_LENGTH;
    //# dynamic URI status
    bool dynamicUri;
    // the contract owner
    // not part of the core spec but a common feature for NFT projects
    address public owner;
    // pause status True / False
    // not part of the core spec but a common feature for NFT projects
    bool public paused;
    // the contracts URI to find the metadata
    string[MAX_URI_LENGTH] baseuri;
    string[MAX_URI_LENGTH] public contractURI;
    // Name and symbol are not part of the ERC1155 standard. For opensea compatibility
    string[128] public name;
    string[16] public symbol;
    // Interface IDs
    bytes4 constant ERC165_INTERFACE_ID = 0x01ffc9a7;
    bytes4 constant ERC1155_INTERFACE_ID = 0xd9b67a26;
    bytes4 constant ERC1155_INTERFACE_ID_METADATA = 0x0e89341c;
    // mappings
    // Mapping from token ID to account balances
    mapping (address => mapping (uint256 => uint256)) public balanceOf;
    // Mapping from account to operator approvals
    mapping (address => mapping (address => bool)) public isApprovedForAll;
    //############## events ###############
    // Emits a pause event with the address that paused the contract
    event Paused(address account);

    // Emits an unpause event with the address that paused the contract
    event unPaused(address account);

    // Emits smart contract ownership transfer from current to new owner
    event OwnershipTransferred(address previouwOwner, address newOwner);

    // Emits on transfer of a single token
    event TransferSingle(address indexed operator, address indexed fromAddress, address indexed to, uint256 id, uint256 value);

    // Emits on batch transfer of tokens. the ids array correspond with the values array by their position
    //# indexed
    event TransferBatch(address indexed operator, address indexed fromAddress, address indexed to, uint256[] ids, uint256[] values);

    // This emits when an operator is enabled or disabled for an owner. The operator manages all tokens for an owner
    event ApprovalForAll(address indexed account, address indexed operator, bool approved);

    // This emits when the URI gets changed
    event URI(string[MAX_URI_LENGTH] value, uint256 id);

    //############## interfaces ###############
    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC165
    //############## functions ###############
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev contract initialization on deployment
    @dev will set name and symbol, interfaces, owner and URI
    @dev self.paused will default to false
    @param name the smart contract name
    @param symbol the smart contract symbol
    @param uri the new uri for the contract
    */
    constructor (string[128] name, string[16] symbol, string[MAX_URI_LENGTH] uri, string[MAX_URI_LENGTH] contractUri) private external
    {
        name = name;
        symbol = symbol;
        owner = msg.sender;
        baseuri = uri;
        contractURI = contractUri;
    }


    //# contract status ##
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Pause the contract, checks if the caller is the owner and if the contract is paused already
    @dev emits a pause event 
    @dev not part of the core spec but a common feature for NFT projects
    */
    function pause() public external
    {
        require(
            owner == msg.sender,
            "Ownable: caller is not the owner"
        );
        require(
            !paused,
            "the contract is already paused"
        );
        paused = true;
        emit Paused(msg.sender);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Unpause the contract, checks if the caller is the owner and if the contract is paused already
    @dev emits an unpause event 
    @dev not part of the core spec but a common feature for NFT projects
    */
    function unpause() public external
    {
        require(
            owner == msg.sender,
            "Ownable: caller is not the owner"
        );
        require(
            paused,
            "the contract is not paused"
        );
        paused = false;
        emit unPaused(msg.sender);
    }


    //# ownership ##
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Transfer the ownership. Checks for contract pause status, current owner and prevent transferring to
    @dev zero address
    @dev emits an OwnershipTransferred event with the old and new owner addresses
    @param newOwner The address of the new owner.
    */
    function transferOwnership(address newOwner) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            owner == msg.sender,
            "Ownable: caller is not the owner"
        );
        require(
            newOwner != owner,
            "This account already owns the contract"
        );
        require(
            newOwner != address(0),
            "Transfer to the zero address not allowed. Use renounceOwnership() instead."
        );
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Transfer the ownership to the zero address, this will lock the contract
    @dev emits an OwnershipTransferred event with the old and new zero owner addresses
    */
    function renounceOwnership() public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            owner == msg.sender,
            "Ownable: caller is not the owner"
        );
        address oldOwner = owner;
        owner = address(0);
        emit OwnershipTransferred(oldOwner, address(0));
    }


    // ##### VYPER DECORATORS #####
    // @external
    // @view
    /**
    @dev check the balance for an array of specific IDs and addresses
    @dev will return an array of balances
    @dev Can also be used to check ownership of an ID
    @param accounts a dynamic array of the addresses to check the balance for
    @param ids a dynamic array of the token IDs to check the balance
    */
    function balanceOfBatch(address[] accounts, uint256[] ids) public external view returns (uint256[])
    {
        require(
            len(accounts) == len(ids),
            "ERC1155: accounts and ids length mismatch"
        );
        uint256[] batchBalances = [];
        uint256 j = 0;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (/*i in ids */) {
            batchBalances.append(balanceOf[accounts[j]][i]);
            j += 1;
        }


        return batchBalances;
    }


    //# mint ##
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev mint one new token with a certain ID
    @dev this can be a new token or "topping up" the balance of a non-fungible token ID
    @param receiver the account that will receive the minted token
    @param id the ID of the token
    @param amount of tokens for this ID
    @param data the data associated with this mint. Usually stays empty
    */
    function mint(address receiver, uint256 id, uint256 amount, bytes32 data) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            owner == msg.sender,
            "Only the contract owner can mint"
        );
        require(
            receiver != address(0),
            "Can not mint to ZERO ADDRESS"
        );
        address operator = msg.sender;
        balanceOf[receiver][id] += amount;
        emit TransferSingle(operator, address(0), receiver, id, amount);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev mint a batch of new tokens with the passed IDs
    @dev this can be new tokens or "topping up" the balance of existing non-fungible token IDs in the contract
    @param receiver the account that will receive the minted token
    @param ids array of ids for the tokens
    @param amounts amounts of tokens for each ID in the ids array
    @param data the data associated with this mint. Usually stays empty
    */
    function mintBatch(address receiver, uint256[] ids, uint256[] amounts, bytes32 data) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            owner == msg.sender,
            "Only the contract owner can mint"
        );
        require(
            receiver != address(0),
            "Can not mint to ZERO ADDRESS"
        );
        require(
            len(ids) == len(amounts),
            "ERC1155: ids and amounts length mismatch"
        );
        address operator = msg.sender;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < BATCH_SIZE; i++) {
            if (i >= len(ids)) {
                break;
            }
            balanceOf[receiver][ids[i]] += amounts[i];
        }


        emit TransferBatch(operator, address(0), receiver, ids, amounts);
    }


    //# burn ##
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev burn one or more token with a certain ID
    @dev the amount of tokens will be deducted from the holder's balance
    @param id the ID of the token to burn
    @param amount of tokens to burnfor this ID
    */
    function burn(uint256 id, uint256 amount) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            balanceOf[msg.sender][id] > 0,
            "caller does not own this ID"
        );
        balanceOf[msg.sender][id] -= amount;
        emit TransferSingle(msg.sender, msg.sender, address(0), id, amount);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev burn a batch of tokens with the passed IDs
    @dev this can be burning non fungible tokens or reducing the balance of existing non-fungible token IDs in the contract
    @dev inside the loop ownership will be checked for each token. We can not burn tokens we do not own
    @param ids array of ids for the tokens to burn
    @param amounts array of amounts of tokens for each ID in the ids array
    */
    function burnBatch(uint256[] ids, uint256[] amounts) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            len(ids) == len(amounts),
            "ERC1155: ids and amounts length mismatch"
        );
        address operator = msg.sender;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < BATCH_SIZE; i++) {
            if (i >= len(ids)) {
                break;
            }
            balanceOf[msg.sender][ids[i]] -= amounts[i];
        }


        emit TransferBatch(msg.sender, msg.sender, address(0), ids, amounts);
    }


    //# approval ##
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev set an operator for a certain NFT owner address
    @param owner the NFT owner address
    @param operator the operator address
    @param approved approve or disapprove
    */
    function setApprovalForAll(address owner, address operator, bool approved) public external
    {
        require(
            owner == msg.sender,
            "You can only set operators for your own account"
        );
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            owner != operator,
            "ERC1155: setting approval status for self"
        );
        isApprovedForAll[owner][operator] = approved;
        emit ApprovalForAll(owner, operator, approved);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev transfer token from one address to another.
    @param sender the sending account (current owner)
    @param receiver the receiving account
    @param id the token id that will be sent
    @param amount the amount of tokens for the specified id
    */
    function safeTransferFrom(address sender, address receiver, uint256 id, uint256 amount, bytes32 bytes) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            receiver != address(0),
            "ERC1155: transfer to the zero address"
        );
        require(sender != receiver);
        require(
            sender == msg.sender || isApprovedForAll[sender][msg.sender],
            "Caller is neither owner nor approved operator for this ID"
        );
        require(
            balanceOf[sender][id] > 0,
            "caller does not own this ID or ZERO balance"
        );
        address operator = msg.sender;
        balanceOf[sender][id] -= amount;
        balanceOf[receiver][id] += amount;
        emit TransferSingle(operator, sender, receiver, id, amount);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev transfer tokens from one address to another.
    @param sender the sending account
    @param receiver the receiving account
    @param ids a dynamic array of the token ids that will be sent
    @param amounts a dynamic array of the amounts for the specified list of ids.
    */
    function safeBatchTransferFrom(address sender, address receiver, uint256[] ids, uint256[] amounts, bytes32 _bytes) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            receiver != address(0),
            "ERC1155: transfer to the zero address"
        );
        require(sender != receiver);
        require(
            sender == msg.sender || isApprovedForAll[sender][msg.sender],
            "Caller is neither owner nor approved operator for this ID"
        );
        require(
            len(ids) == len(amounts),
            "ERC1155: ids and amounts length mismatch"
        );
        address operator = msg.sender;
        
        // TODO: CHECK THE LOOP AND ITS VARIABLES
        for (uint i = 0; i < BATCH_SIZE; i++) {
            if (i >= len(ids)) {
                break;
            }
            uint256 id = ids[i];
            uint256 amount = amounts[i];
            balanceOf[sender][id] -= amount;
            balanceOf[receiver][id] += amount;
        }


        emit TransferBatch(operator, sender, receiver, ids, amounts);
    }


    // URI #
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev set the URI for the contract
    @param uri the new uri for the contract
    */
    function setURI(string[MAX_URI_LENGTH] uri) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            baseuri != uri,
            "new and current URI are identical"
        );
        require(
            msg.sender == owner,
            "Only the contract owner can update the URI"
        );
        baseuri = uri;
        emit URI(uri, 0);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev toggle dynamic URI
    @param status true for dynamic false for static
    */
    function toggleDynUri(bool status) public external
    {
        require(msg.sender == owner);
        require(
            status != dynamicUri,
            "already in desired state"
        );
        dynamicUri = status;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    /**
    @dev retrieve the uri. Adds requested ID when dynamic URI is active
    @param id NFT ID to retrieve the uri for. 
    */
    function uri(uint256 id) public external view returns (string[MAX_URL_LENGTH])
    {
        if (dynamicUri) {
            return concat(baseuri, uint2str(id), '.json');
        }
    }


    // URI #
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev set the contractURI for the contract. points to collection metadata file
    @dev This function is opensea specific and is required to properly show collection metadata and image
    @param contractUri the new urcontractUri for the contract
    */
    function setContractURI(string[MAX_URI_LENGTH] contractUri) public external
    {
        require(
            !paused,
            "The contract has been paused"
        );
        require(
            contractURI != contractUri,
            "new and current URI are identical"
        );
        require(
            msg.sender == owner,
            "Only the contract owner can update the URI"
        );
        contractURI = contractUri;
        emit URI(contractUri, 0);
    }


    // ##### VYPER DECORATORS #####
    // @pure
    // @external
    /**
    @dev Returns True if the interface is supported
    @param interfaceId bytes4 interface identifier
    */
    function supportsInterface(bytes4 interfaceId) public external pure returns (bool)
    {
        return /* TODO: CHECK 'IN' CONDITION interfaceId in [ERC165_INTERFACE_ID,ERC1155_INTERFACE_ID,ERC1155_INTERFACE_ID_METADATA,] */;
    }



}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
// TODO: fromvyper.interfacesimportERC165
