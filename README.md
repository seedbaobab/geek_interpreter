# Geek Interpreter
## Introduction
As its name suggests, this project is an interpreter which aims to interpret the **Geek** language. This
latter is a simple language for calling API services, either by its provider.

## Call
Calling a service from the interpreter is simple, all you have to do is call the provider and the desired service with the
necessary arguments. Example: <code>provider.service("arg1", 10)</code>.

The grammar of the language is quite simple, it is defined below.

### Grammar
<code>axiom -> appel_api</code><br/>
<code>axiom -> appel_provider</code>

<code>appel_api -> identifiant'.'appel_provider</code>

<code>appel_provider -> identifiant'.'appel_service</code>

<code>appel_service -> identifiant'('')'</code>
<code>appel_service -> identifiant'('liste_arguments')'</code>

<code>liste_arguments -> expression sous_liste_argument</code>

<code>sous_liste_argument -> ∅</code><br/>
<code>sous_liste_argument -> ',' expression sous_liste_argument</code>

<code>expression -> entier</code><br/>
<code>expression -> chaine_de_caractères</code><br/>