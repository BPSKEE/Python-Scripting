% reverse list function to recursively add the head of a list to the tail
reverse_list([], []).
reverse_list([H|T], Reversed) :-
    reverse_list(T, Rest),
    append(Rest, [H], Reversed).

% run reversed list function off of input array
main :-
    read(InputList),
    reverse_list(InputList, Reversed),
    write(Reversed), nl.