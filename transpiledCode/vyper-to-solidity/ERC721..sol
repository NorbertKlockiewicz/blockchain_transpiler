interface ERC721Receiver {
    function onERC721Received(address _operator, address _from, uint256 _tokenId, bytes[1024] _data) public external view returns (bytes4);
}
pragma solidity >=0.4.0 <0.9.0;

contract FromVyper {
    // @dev Implementation of ERC-721 non-fungible token standard.
    // @author Ryuya Nakamura (@nrryuya)
    // Modified from: https://github.com/vyperlang/vyper/blob/de74722bf2d8718cca46902be165f9fe0e3641dd/examples/tokens/ERC721.vy


    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC721
    // TODO: FIX INTERFACE IMPLEMENTATION implements: ERC165
    // Interface for the contract called by safeTransferFrom()
    // @dev Emits when ownership of any NFT changes by any mechanism. This event emits when NFTs are
    //      created (`from` == 0) and destroyed (`to` == 0). Exception: during contract creation, any
    //      number of NFTs may be created and assigned without emitting Transfer. At the time of any
    //      transfer, the approved address for that NFT (if any) is reset to none.
    // @param _from Sender of NFT (if address is zero address it indicates token creation).
    // @param _to Receiver of NFT (if address is zero address it indicates token destruction).
    // @param _tokenId The NFT that got transfered.
    event Transfer(address indexed sender, address indexed receiver, uint256 indexed tokenId);

    // @dev This emits when the approved address for an NFT is changed or reaffirmed. The zero
    //      address indicates there is no approved address. When a Transfer event emits, this also
    //      indicates that the approved address for that NFT (if any) is reset to none.
    // @param _owner Owner of NFT.
    // @param _approved Address that we are approving.
    // @param _tokenId NFT which we are approving.
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);

    // @dev This emits when an operator is enabled or disabled for an owner. The operator can manage
    //      all NFTs of the owner.
    // @param _owner Owner of NFT.
    // @param _operator Address to which we are setting operator rights.
    // @param _approved Status of operator rights(true if operator rights are given and false if
    // revoked).
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);

    // @dev Mapping from NFT ID to the address that owns it.
    mapping (uint256 => address) idToOwner;
    // @dev Mapping from NFT ID to approved address.
    mapping (uint256 => address) idToApprovals;
    // @dev Mapping from owner address to count of his tokens.
    mapping (address => uint256) ownerToNFTokenCount;
    // @dev Mapping from owner address to mapping of operator addresses.
    mapping (address => mapping (address => bool)) ownerToOperators;
    // @dev Address of minter, who can mint a token
    address minter;
    string[53] baseURL;
    // @dev Static list of supported ERC165 interface ids
    bytes4[2] constant SUPPORTED_INTERFACES = [// ERC165 interface ID of ERC165
    0x01ffc9a7,// ERC165 interface ID of ERC721
    0x80ac58cd];
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Contract constructor.
    */
    constructor () private external
    {
        minter = msg.sender;
        baseURL = "https://api.babby.xyz/metadata/";
    }


    // ##### VYPER DECORATORS #####
    // @pure
    // @external
    /**
    @dev Interface identification is specified in ERC-165.
    @param interface_id Id of the interface
    */
    function supportsInterface(bytes4 interface_id) public external pure returns (bool)
    {
        return /* TODO: CHECK 'IN' CONDITION interface_id in SUPPORTED_INTERFACES */;
    }


    //## VIEW FUNCTIONS ###
    // ##### VYPER DECORATORS #####
    // @view
    // @external
    /**
    @dev Returns the number of NFTs owned by `_owner`.
         Throws if `_owner` is the zero address. NFTs assigned to the zero address are considered invalid.
    @param _owner Address for whom to query the balance.
    */
    function balanceOf(address _owner) public external view returns (uint256)
    {
        require(_owner != address(0));
        return ownerToNFTokenCount[_owner];
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    /**
    @dev Returns the address of the owner of the NFT.
         Throws if `_tokenId` is not a valid NFT.
    @param _tokenId The identifier for an NFT.
    */
    function ownerOf(uint256 _tokenId) public external view returns (address)
    {
        address owner = idToOwner[_tokenId];
        // Throws if `_tokenId` is not a valid NFT
        require(owner != address(0));
        return owner;
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    /**
    @dev Get the approved address for a single NFT.
         Throws if `_tokenId` is not a valid NFT.
    @param _tokenId ID of the NFT to query the approval of.
    */
    function getApproved(uint256 _tokenId) public external view returns (address)
    {
        // Throws if `_tokenId` is not a valid NFT
        require(idToOwner[_tokenId] != address(0));
        return idToApprovals[_tokenId];
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    /**
    @dev Checks if `_operator` is an approved operator for `_owner`.
    @param _owner The address that owns the NFTs.
    @param _operator The address that acts on behalf of the owner.
    */
    function isApprovedForAll(address _owner, address _operator) public external view returns (bool)
    {
        return (ownerToOperators[_owner])[_operator];
    }


    //## TRANSFER FUNCTION HELPERS ###
    // ##### VYPER DECORATORS #####
    // @view
    // @internal
    /**
    @dev Returns whether the given spender can transfer a given token ID
    @param spender address of the spender to query
    @param tokenId uint256 ID of the token to be transferred
    @return bool whether the msg.sender is approved for the given token ID,
        is an operator of the owner, or is the owner of the token
    */
    function _isApprovedOrOwner(address _spender, uint256 _tokenId) private internal view returns (bool)
    {
        address owner = idToOwner[_tokenId];
        bool spenderIsOwner = owner == _spender;
        bool spenderIsApproved = _spender == idToApprovals[_tokenId];
        bool spenderIsApprovedForAll = (ownerToOperators[owner])[_spender];
        return (spenderIsOwner || spenderIsApproved) || spenderIsApprovedForAll;
    }


    // ##### VYPER DECORATORS #####
    // @internal
    /**
    @dev Add a NFT to a given address
         Throws if `_tokenId` is owned by someone.
    */
    function _addTokenTo(address _to, uint256 _tokenId) private internal
    {
        // Throws if `_tokenId` is owned by someone
        require(idToOwner[_tokenId] == address(0));
        // Change the owner
        idToOwner[_tokenId] = _to;
        // Change count tracking
        ownerToNFTokenCount[_to] += 1;
    }


    // ##### VYPER DECORATORS #####
    // @internal
    /**
    @dev Remove a NFT from a given address
         Throws if `_from` is not the current owner.
    */
    function _removeTokenFrom(address _from, uint256 _tokenId) private internal
    {
        // Throws if `_from` is not the current owner
        require(idToOwner[_tokenId] == _from);
        // Change the owner
        idToOwner[_tokenId] = address(0);
        // Change count tracking
        ownerToNFTokenCount[_from] -= 1;
    }


    // ##### VYPER DECORATORS #####
    // @internal
    /**
    @dev Clear an approval of a given address
         Throws if `_owner` is not the current owner.
    */
    function _clearApproval(address _owner, uint256 _tokenId) private internal
    {
        // Throws if `_owner` is not the current owner
        require(idToOwner[_tokenId] == _owner);
        if (idToApprovals[_tokenId] != address(0)) {
            // Reset approvals
            idToApprovals[_tokenId] = address(0);
        }
    }


    // ##### VYPER DECORATORS #####
    // @internal
    /**
    @dev Exeute transfer of a NFT.
         Throws unless `msg.sender` is the current owner, an authorized operator, or the approved
         address for this NFT. (NOTE: `msg.sender` not allowed in private function so pass `_sender`.)
         Throws if `_to` is the zero address.
         Throws if `_from` is not the current owner.
         Throws if `_tokenId` is not a valid NFT.
    */
    function _transferFrom(address _from, address _to, uint256 _tokenId, address _sender) private internal
    {
        // Check requirements
        require(_isApprovedOrOwner(_sender, _tokenId));
        // Throws if `_to` is the zero address
        require(_to != address(0));
        // Clear approval. Throws if `_from` is not the current owner
        _clearApproval(_from, _tokenId);
        // Remove NFT. Throws if `_tokenId` is not a valid NFT
        _removeTokenFrom(_from, _tokenId);
        // Add NFT
        _addTokenTo(_to, _tokenId);
        // Log the transfer
        emit Transfer(_from, _to, _tokenId);
    }


    //## TRANSFER FUNCTIONS ###
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Throws unless `msg.sender` is the current owner, an authorized operator, or the approved
         address for this NFT.
         Throws if `_from` is not the current owner.
         Throws if `_to` is the zero address.
         Throws if `_tokenId` is not a valid NFT.
    @notice The caller is responsible to confirm that `_to` is capable of receiving NFTs or else
            they maybe be permanently lost.
    @param _from The current owner of the NFT.
    @param _to The new owner.
    @param _tokenId The NFT to transfer.
    */
    function transferFrom(address _from, address _to, uint256 _tokenId) public external
    {
        _transferFrom(_from, _to, _tokenId, msg.sender);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Transfers the ownership of an NFT from one address to another address.
         Throws unless `msg.sender` is the current owner, an authorized operator, or the
         approved address for this NFT.
         Throws if `_from` is not the current owner.
         Throws if `_to` is the zero address.
         Throws if `_tokenId` is not a valid NFT.
         If `_to` is a smart contract, it calls `onERC721Received` on `_to` and throws if
         the return value is not `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`.
    @param _from The current owner of the NFT.
    @param _to The new owner.
    @param _tokenId The NFT to transfer.
    @param _data Additional data with no specified format, sent in call to `_to`.
    */
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes[1024] _data = bytes("")) public external
    {
        _transferFrom(_from, _to, _tokenId, msg.sender);
        if (_to.is_contract) {
            bytes4 returnValue = ERC721Receiver(_to).onERC721Received(msg.sender, _from, _tokenId, _data);
            // Throws if transfer destination is a contract which does not implement 'onERC721Received'
            require(returnValue == method_id("onERC721Received(address,address,uint256,bytes)", output_type = bytes4));
        }
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Set or reaffirm the approved address for an NFT. The zero address indicates there is no approved address.
         Throws unless `msg.sender` is the current NFT owner, or an authorized operator of the current owner.
         Throws if `_tokenId` is not a valid NFT. (NOTE: This is not written the EIP)
         Throws if `_approved` is the current owner. (NOTE: This is not written the EIP)
    @param _approved Address to be approved for the given NFT ID.
    @param _tokenId ID of the token to be approved.
    */
    function approve(address _approved, uint256 _tokenId) public external
    {
        address owner = idToOwner[_tokenId];
        // Throws if `_tokenId` is not a valid NFT
        require(owner != address(0));
        // Throws if `_approved` is the current owner
        require(_approved != owner);
        // Check requirements
        bool senderIsOwner = idToOwner[_tokenId] == msg.sender;
        bool senderIsApprovedForAll = (ownerToOperators[owner])[msg.sender];
        require((senderIsOwner || senderIsApprovedForAll));
        // Set the approval
        idToApprovals[_tokenId] = _approved;
        emit Approval(owner, _approved, _tokenId);
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Enables or disables approval for a third party ("operator") to manage all of
         `msg.sender`'s assets. It also emits the ApprovalForAll event.
         Throws if `_operator` is the `msg.sender`. (NOTE: This is not written the EIP)
    @notice This works even if sender doesn't own any tokens at the time.
    @param _operator Address to add to the set of authorized operators.
    @param _approved True if the operators is approved, false to revoke approval.
    */
    function setApprovalForAll(address _operator, bool _approved) public external
    {
        // Throws if `_operator` is the `msg.sender`
        require(_operator != msg.sender);
        ownerToOperators[msg.sender][_operator] = _approved;
        emit ApprovalForAll(msg.sender, _operator, _approved);
    }


    //## MINT & BURN FUNCTIONS ###
    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Function to mint tokens
         Throws if `msg.sender` is not the minter.
         Throws if `_to` is zero address.
         Throws if `_tokenId` is owned by someone.
    @param _to The address that will receive the minted tokens.
    @param _tokenId The token id to mint.
    @return A boolean that indicates if the operation was successful.
    */
    function mint(address _to, uint256 _tokenId) public external returns (bool)
    {
        // Throws if `msg.sender` is not the minter
        require(msg.sender == minter);
        // Throws if `_to` is zero address
        require(_to != address(0));
        // Add NFT. Throws if `_tokenId` is owned by someone
        _addTokenTo(_to, _tokenId);
        emit Transfer(address(0), _to, _tokenId);
        return true;
    }


    // ##### VYPER DECORATORS #####
    // @external
    /**
    @dev Burns a specific ERC721 token.
         Throws unless `msg.sender` is the current owner, an authorized operator, or the approved
         address for this NFT.
         Throws if `_tokenId` is not a valid NFT.
    @param _tokenId uint256 id of the ERC721 token to be burned.
    */
    function burn(uint256 _tokenId) public external
    {
        // Check requirements
        require(_isApprovedOrOwner(msg.sender, _tokenId));
        address owner = idToOwner[_tokenId];
        // Throws if `_tokenId` is not a valid NFT
        require(owner != address(0));
        _clearApproval(owner, _tokenId);
        _removeTokenFrom(owner, _tokenId);
        emit Transfer(owner, address(0), _tokenId);
    }


    // ##### VYPER DECORATORS #####
    // @view
    // @external
    function tokenURI(uint256 tokenId) public external view returns (string[132])
    {
        return concat(baseURL, uint2str(tokenId));
    }



}

//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########
// TODO: fromvyper.interfacesimportERC165
// TODO: fromvyper.interfacesimportERC721
