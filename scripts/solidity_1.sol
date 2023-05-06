// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;


contract OwnedToken {
    // TokenCreator est un type de contrat défini ci-dessous.
    // Il est possible de le référencer tant qu'il n'est pas utilisé
    // pour créer un nouveau contrat.
    TokenCreator creator;
    address owner;
    bytes32 name;

    // This is the constructor which registers the
    // creator and the assigned name.
    constructor(bytes32 _name) {
        // State variables are accessed via their name
        // and not via e.g. `this.owner`. Functions can
        // be accessed directly or through `this.f`,
        // but the latter provides an external view
        // to the function. Especially in the constructor,
        // you should not access functions externally,
        // because the function does not exist yet.
        // See the next section for details.
        owner = msg.sender;
        // Nous effectuons une conversion de type explicite de `address`.
        // vers `TokenCreator` et supposons que le type du
        // contrat appelant est TokenCreator,
        // Il n'y a pas vraiment moyen de vérifier ça.
        creator = TokenCreator(msg.sender);
        name = _name;
    }

    function changeName(bytes32 newName) public {
        // Seul le créateur peut modifier le nom --
        // la comparaison est possible puisque les contrats
        // sont explicitement convertibles en adresses.
        if (msg.sender == address(creator))
            name = newName;
    }

    function transfer(address newOwner) public {
        // Seul le propriétaire actuel peut transférer le token.
        if (msg.sender != owner) return;

        // Nous voulons aussi demander au créateur si le transfert
        // est valide. Notez que ceci appelle une fonction de la fonction
        // contrat défini ci-dessous. Si l'appel échoue (p. ex.
        // en raison d'un manque de gas), l'exécution échoue également ici.
        if (creator.isTokenTransferOK(owner, newOwner))
            owner = newOwner;
    }
}

contract TokenCreator {
    function createToken(bytes32 name)
       public
       returns (OwnedToken tokenAddress)
    {
        // Créer un nouveau contrat Token et renvoyer son adresse.
        // Du côté JavaScript, le type de retour est simplement
        // `address`, car c'est le type le plus proche disponible dans
        // l'ABI.
        return new OwnedToken(name);
    }

    function changeName(OwnedToken tokenAddress, bytes32 name) public {
        // Encore une fois, le type externe de `tokenAddress' est
        // simplement `adresse`.
        tokenAddress.changeName(name);
    }

    function isTokenTransferOK(address currentOwner, address newOwner)
        public
        pure
        returns (bool ok)
    {
        // Vérifier une condition arbitraire.
        return keccak256(abi.encodePacked(currentOwner, newOwner))[0] == 0x7f;
    }
}