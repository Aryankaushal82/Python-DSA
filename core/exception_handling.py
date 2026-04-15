"""
===============================
PYTHON EXCEPTION HANDLING NOTES
===============================

1. WHAT IS EXCEPTION HANDLING?
------------------------------
Exception handling is used to handle runtime errors so that
the program does not crash unexpectedly.

It allows controlled flow of execution when an error occurs.


2. BASIC SYNTAX
---------------
try:
    # risky code
except SomeException:
    # handle error
else:
    # runs if no exception
finally:
    # always runs


3. EXECUTION FLOW
-----------------
1. try block executes
2. If exception occurs → matching except executes
3. If no exception → else executes
4. finally executes ALWAYS (with or without error)


4. TRY BLOCK
------------
- Contains code that may cause an exception
- Keep it minimal (only risky code)


5. EXCEPT BLOCK
---------------
- Handles exceptions

Specific exception:
    except ValueError:

Multiple exceptions:
    except (ValueError, TypeError):

Generic (not recommended unless needed):
    except Exception as err:
        print(err)


6. ELSE BLOCK
-------------
- Executes only if NO exception occurs
- Used for success logic


7. FINALLY BLOCK
----------------
- Executes ALWAYS
- Used for cleanup (closing files, releasing resources)


8. COMMON EXCEPTIONS
--------------------
ValueError           → Invalid value (e.g., wrong conversion)
TypeError            → Invalid operation between types
ZeroDivisionError    → Division by zero
IndexError           → Invalid index
KeyError             → Missing dictionary key
FileNotFoundError    → File not found


9. EXCEPTION OBJECT
-------------------
except Exception as err:
    print(err)

- err contains error message/details


10. RAISING EXCEPTIONS
----------------------
- Used to manually trigger errors

Example:
    raise ValueError("Invalid input")

Used for logical validation conditions.


11. MULTIPLE EXCEPT BLOCKS
--------------------------
- Checked from top to bottom
- Always place specific exceptions first

Example:
    try:
        pass
    except ValueError:
        pass
    except Exception:
        pass


12. IMPORTANT RULES
-------------------
- Do NOT overuse generic except
- Catch only what you can handle
- Keep try block small
- Use finally for cleanup
- Use raise for validation logic


13. EXIT BEHAVIOR
-----------------
- exit() or sys.exit() stops program
- finally block still executes


14. CLEAN TEMPLATE
------------------
try:
    # risky operation
    pass

except SpecificError:
    # handle specific case
    pass

except Exception as err:
    # fallback handler
    print(err)

else:
    # success path
    pass

finally:
    # cleanup code
    pass


15. MENTAL MODEL
----------------
try     → attempt
except  → handle failure
else    → success path
finally → cleanup


END OF NOTES
"""